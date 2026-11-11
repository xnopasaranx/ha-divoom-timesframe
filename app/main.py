from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import json
import requests

from .config import Config

app = FastAPI(title="Divoom TimesFrame Test UI")

ROOT = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(ROOT / "templates"))
config = Config()

# Domain-specific defaults for common fields.
FIELD_DEFAULTS = {
    "OnOff": 1,
    "Brightness": 80,
    "ClockId": 657,
    "Text": "Hello Divoom",
    "TextColor": "#ff0000",
    "DeviceId": config.device_id,
    "UserId": 1,
    "StartNum": 1,
    "EndNum": 20,
    "LcdIndex": 1,
    "PageIndex": 1,
    "Flag": 0,
    "Version": 0,
}


def default_for_field(field: dict):
    name = field.get("json_name")
    if name == "DeviceId":
        return config.device_id
    if name in FIELD_DEFAULTS:
        return FIELD_DEFAULTS[name]
    t = field.get("type", "")
    if "int" in t or "long" in t:
        return 0
    if "boolean" in t or "Boolean" in t:
        return False
    if "String" in t:
        return ""
    if "List" in t:
        return []
    return None


def load_schemas() -> dict[str, dict]:
    schema_file = ROOT / ".." / "endpoint_schemas.json"
    if not schema_file.exists():
        return {}
    data = json.loads(schema_file.read_text())
    return data.get("commands", {})


def load_command_list() -> list[str]:
    cmd_file = ROOT / "commands.txt"
    if cmd_file.exists():
        return [
            line.strip()
            for line in cmd_file.read_text().splitlines()
            if line.strip() and "failed" not in line.lower()
        ]
    return []


SCHEMAS = load_schemas()
COMMANDS = load_command_list()


def payload_template(command: str) -> dict:
    schema = SCHEMAS.get(command, {})
    template = {}
    for field in schema.get("own_fields", []):
        template[field["json_name"]] = default_for_field(field)
    return template


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    commands_data = []
    for cmd in COMMANDS:
        schema = SCHEMAS.get(cmd, {})
        commands_data.append(
            {
                "command": cmd,
                "category": schema.get("category", cmd.split("/", 1)[0]),
                "purpose": schema.get("purpose", ""),
                "template": payload_template(cmd),
                "request_fields": schema.get("request_fields", []),
                "own_fields": schema.get("own_fields", []),
                "response_fields": schema.get("response_fields", []),
                "request_class": schema.get("request_class"),
                "response_class": schema.get("response_class"),
            }
        )
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "device_url": config.base_url,
            "commands": commands_data,
            "settings": config.as_dict(),
        },
    )


@app.get("/api/settings")
def get_settings():
    return config.as_dict()


@app.post("/api/settings")
def update_settings(body: dict):
    ip = body.get("device_ip", "").strip()
    port = body.get("device_port", 9000)
    device_id = body.get("device_id", 0)

    if not ip:
        return JSONResponse({"error": "Device IP is required"}, status_code=400)
    try:
        port = int(port)
        device_id = int(device_id)
    except (TypeError, ValueError):
        return JSONResponse({"error": "Port and Device ID must be numbers"}, status_code=400)

    config.device_ip = ip
    config.device_port = port
    config.device_id = device_id
    FIELD_DEFAULTS["DeviceId"] = device_id
    config.save()

    return config.as_dict()


@app.get("/api/schemas")
def list_schemas():
    return {
        "device_url": config.base_url,
        "commands": [
            {
                "command": c,
                "category": SCHEMAS.get(c, {}).get("category", c.split("/", 1)[0]),
                "purpose": SCHEMAS.get(c, {}).get("purpose", ""),
                "template": payload_template(c),
                "request_fields": SCHEMAS.get(c, {}).get("request_fields", []),
                "own_fields": SCHEMAS.get(c, {}).get("own_fields", []),
                "response_fields": SCHEMAS.get(c, {}).get("response_fields", []),
                "request_class": SCHEMAS.get(c, {}).get("request_class"),
                "response_class": SCHEMAS.get(c, {}).get("response_class"),
            }
            for c in COMMANDS
        ],
    }


@app.get("/api/commands")
def list_commands():
    return {
        "device_url": config.base_url,
        "commands": [
            {
                "command": c,
                "category": SCHEMAS.get(c, {}).get("category", c.split("/", 1)[0]),
                "template": payload_template(c),
            }
            for c in COMMANDS
        ],
    }


@app.post("/api/send")
def send_command(body: dict):
    command = body.get("command")
    payload = body.get("payload", {})
    if not command:
        return JSONResponse({"error": "Missing 'command'"}, status_code=400)

    full_payload = {"Command": command}
    full_payload.update(payload)

    try:
        resp = requests.get(
            config.base_url,
            json=full_payload,
            timeout=10,
            headers={"Content-Type": "application/json"},
        )
        try:
            data = resp.json()
        except Exception:
            data = {"status_code": resp.status_code, "text": resp.text}
        return {
            "request": full_payload,
            "status_code": resp.status_code,
            "response": data,
        }
    except requests.exceptions.Timeout:
        return JSONResponse(
            {
                "request": full_payload,
                "error": "Request timed out. Some commands (e.g. SetClockSelectId) take several seconds.",
            },
            status_code=504,
        )
    except Exception as exc:
        return JSONResponse(
            {"request": full_payload, "error": str(exc)}, status_code=502
        )


@app.get("/api/clocklist")
def cloud_clock_list():
    """Proxy Divoom cloud clock list so the UI can show valid ClockIds."""
    try:
        resp = requests.get(
            "https://appin.divoom-gz.com/Channel/MyClockGetList",
            params={
                "DeviceId": config.device_id,
                "StartNum": 1,
                "EndNum": 100,
                "DeviceType": "Frame",
            },
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        return resp.json()
    except Exception as exc:
        return JSONResponse({"error": str(exc)}, status_code=502)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
