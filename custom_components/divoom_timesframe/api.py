"""Async API client for Divoom TimesFrame."""
from __future__ import annotations

import logging
from typing import Any

import aiohttp

from .const import DEFAULT_PORT, DEFAULT_TIMEOUT

_LOGGER = logging.getLogger(__name__)


class DivoomTimesFrameApi:
    """Async client for the Divoom TimesFrame local REST API."""

    def __init__(
        self,
        host: str,
        port: int = DEFAULT_PORT,
        session: aiohttp.ClientSession | None = None,
    ) -> None:
        self.host = host
        self.port = port
        self._base_url = f"http://{host}:{port}/divoom_api"
        self._session = session

    @property
    def base_url(self) -> str:
        return self._base_url

    def _session_or_raise(self) -> aiohttp.ClientSession:
        if self._session is None:
            raise RuntimeError("No aiohttp session provided")
        return self._session

    async def _request(self, payload: dict[str, Any]) -> dict[str, Any]:
        session = self._session_or_raise()
        async with session.get(
            self._base_url,
            json=payload,
            timeout=aiohttp.ClientTimeout(total=DEFAULT_TIMEOUT),
            headers={"Content-Type": "application/json"},
        ) as resp:
            resp.raise_for_status()
            return await resp.json()

    async def get_on_off_screen(self) -> dict[str, Any]:
        return await self._request({"Command": "Channel/GetOnOffScreen"})

    async def set_on_off_screen(self, on: bool) -> dict[str, Any]:
        return await self._request(
            {"Command": "Channel/OnOffScreen", "OnOff": 1 if on else 0}
        )

    async def get_clock_info(self) -> dict[str, Any]:
        return await self._request({"Command": "Channel/GetClockInfo"})

    async def set_brightness(self, brightness: int) -> dict[str, Any]:
        return await self._request(
            {"Command": "Channel/SetBrightness", "Brightness": brightness}
        )

    async def set_clock_select_id(self, clock_id: int) -> dict[str, Any]:
        return await self._request(
            {"Command": "Channel/SetClockSelectId", "ClockId": clock_id}
        )

    async def send_danmaku(
        self, text: str, color: str = "#FFFFFF", user_id: int = 1
    ) -> dict[str, Any]:
        device_id = await self.get_device_id()
        return await self._request(
            {
                "Command": "Danmaku/SendText",
                "DeviceId": device_id,
                "Text": text,
                "TextColor": color,
                "UserId": user_id,
            }
        )

    async def sys_reboot(self) -> dict[str, Any]:
        return await self._request({"Command": "Device/SysReboot"})

    async def get_device_id(self) -> int:
        data = await self.get_on_off_screen()
        return data.get("DeviceId", 0)

    async def probe(self) -> dict[str, Any]:
        """Probe the device and return identifying info."""
        data = await self.get_on_off_screen()
        return {
            "device_id": data.get("DeviceId"),
            "device_type": data.get("DeviceType"),
            "screen_on": data.get("OnOff") == 1,
        }
