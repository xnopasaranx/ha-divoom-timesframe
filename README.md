# Divoom TimesFrame Local API

This repository documents and implements the local REST API of the **Divoom TimesFrame** smart frame.

It contains:

- `ENDPOINTS.md` – full endpoint reference reverse-engineered from the Divoom Android APK
- `app/` – a FastAPI web UI to browse and test every command against a device
- `custom_components/divoom_timesframe/` – a Home Assistant custom integration

## Base URL

```text
http://<device-ip>:9000/divoom_api
```

All calls are HTTP `GET` with a JSON body that always includes `"Command": "<Command>"`.

## FastAPI test UI

Install dependencies and run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn jinja2 requests
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000` and set the **Device settings** (IP, port, Device ID) at the top of the page. Settings are stored in `app/config.json`, which is excluded from git.

Then pick a category and command, edit the JSON payload and send it.

## Home Assistant integration

Copy the integration folder into your Home Assistant configuration:

```bash
cp -r custom_components/divoom_timesframe /path/to/ha/config/custom_components/
```

Restart Home Assistant and add **Divoom TimesFrame** from **Settings → Devices & services → Add integration**.

You can either scan the local network for frames or add a device by IP address.

### Exposed entities per device

- **Switch** – screen on/off
- **Number** – brightness (0-100)
- **Select** – clock face (loaded from Divoom cloud)
- **Sensor** – device info + current clock ID
- **Button** – reboot

### Service

```yaml
service: divoom_timesframe.send_danmaku
data:
  device_id: <DEVICE_ID>
  message: "Hello from Home Assistant!"
  color: "#FF0000"
```

## API documentation

See [`ENDPOINTS.md`](ENDPOINTS.md) for a per-command reference including purpose, request/response classes and JSON fields.

## Reverse-engineering artifacts

The tools, APK and intermediate artifacts used during reverse engineering are kept in `binaries/`. That folder is intentionally excluded from git via `.gitignore`.
