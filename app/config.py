"""Runtime configuration for the Divoom TimesFrame test UI."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class Config:
    """Simple JSON-backed configuration store."""

    def __init__(self, path: Path | None = None) -> None:
        self._path = path or (Path(__file__).resolve().parent / "config.json")
        self._data: dict[str, Any] = {}
        self.load()

    def load(self) -> None:
        if self._path.exists():
            try:
                self._data = json.loads(self._path.read_text(encoding="utf-8"))
                return
            except Exception:
                self._data = {}
        # Defaults when no config file exists.
        self._data = {
            "device_ip": "",
            "device_port": 9000,
            "device_id": 0,
        }

    def save(self) -> None:
        self._path.write_text(
            json.dumps(self._data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    @property
    def device_ip(self) -> str:
        return str(self._data.get("device_ip", ""))

    @device_ip.setter
    def device_ip(self, value: str) -> None:
        self._data["device_ip"] = value

    @property
    def device_port(self) -> int:
        return int(self._data.get("device_port", 9000))

    @device_port.setter
    def device_port(self, value: int) -> None:
        self._data["device_port"] = value

    @property
    def device_id(self) -> int:
        return int(self._data.get("device_id", 0))

    @device_id.setter
    def device_id(self, value: int) -> None:
        self._data["device_id"] = value

    @property
    def base_url(self) -> str:
        return f"http://{self.device_ip}:{self.device_port}/divoom_api"

    def as_dict(self) -> dict[str, Any]:
        return {
            "device_ip": self.device_ip,
            "device_port": self.device_port,
            "device_id": self.device_id,
            "base_url": self.base_url,
        }
