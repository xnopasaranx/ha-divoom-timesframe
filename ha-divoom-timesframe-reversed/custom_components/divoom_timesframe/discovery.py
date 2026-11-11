"""LAN discovery for Divoom TimesFrame devices."""
from __future__ import annotations

import asyncio
import logging
import socket
from typing import Any

import aiohttp

from .const import DEFAULT_PORT

_LOGGER = logging.getLogger(__name__)

PROBE_TIMEOUT = 1.5
MAX_CONCURRENT_PROBES = 30


def _get_local_ip() -> str | None:
    """Return the local IP used for outbound connections."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(2)
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception as exc:
        _LOGGER.debug("Could not determine local IP: %s", exc)
        return None


async def _probe_ip(
    session: aiohttp.ClientSession, ip: str
) -> dict[str, Any] | None:
    """Probe a single IP for a TimesFrame device."""
    url = f"http://{ip}:{DEFAULT_PORT}/divoom_api"
    try:
        async with session.get(
            url,
            json={"Command": "Channel/GetOnOffScreen"},
            timeout=aiohttp.ClientTimeout(total=PROBE_TIMEOUT),
            headers={"Content-Type": "application/json"},
        ) as resp:
            if resp.status != 200:
                return None
            data = await resp.json()
    except Exception:
        return None

    if data.get("DeviceType") != "Frame":
        return None

    return {
        "host": ip,
        "device_id": data.get("DeviceId"),
        "device_type": data.get("DeviceType"),
        "screen_on": data.get("OnOff") == 1,
    }


async def async_discover_devices(
    session: aiohttp.ClientSession,
) -> dict[int, dict[str, Any]]:
    """Scan the local /24 subnet for TimesFrame devices."""
    local_ip = await asyncio.get_event_loop().run_in_executor(None, _get_local_ip)
    if not local_ip:
        _LOGGER.warning("Could not determine local subnet for discovery")
        return {}

    prefix = ".".join(local_ip.split(".")[:3])
    ips = [f"{prefix}.{i}" for i in range(1, 255)]

    semaphore = asyncio.Semaphore(MAX_CONCURRENT_PROBES)

    async def _probe(ip: str) -> dict[str, Any] | None:
        async with semaphore:
            return await _probe_ip(session, ip)

    results = await asyncio.gather(*[_probe(ip) for ip in ips])
    devices: dict[int, dict[str, Any]] = {}
    for result in results:
        if result and result.get("device_id"):
            device_id = int(result["device_id"])
            devices[device_id] = {
                "host": result["host"],
                "device_id": device_id,
                "device_type": result["device_type"],
                "name": f"TimesFrame {device_id}",
            }

    _LOGGER.info("Discovered %s Divoom TimesFrame device(s)", len(devices))
    return devices
