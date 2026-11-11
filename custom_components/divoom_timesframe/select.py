"""Select platform for Divoom TimesFrame clock face."""
from __future__ import annotations

import logging

import aiohttp

from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import CLOUD_CLOCK_LIST_URL, CONF_DEVICE_ID, CONF_DEVICE_TYPE, DOMAIN
from .entity import DivoomTimesFrameEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    data = hass.data[DOMAIN][entry.entry_id]
    clocks = await async_fetch_clock_list(
        hass,
        entry.data[CONF_DEVICE_ID],
        entry.data.get(CONF_DEVICE_TYPE, "Frame"),
    )
    async_add_entities(
        [DivoomClockSelect(data["coordinator"], entry, data["api"], clocks)], True
    )


async def async_fetch_clock_list(hass, device_id: int, device_type: str) -> dict[str, int]:
    """Fetch available clock faces from Divoom cloud."""
    session = async_get_clientsession(hass)
    clocks: dict[str, int] = {}
    try:
        async with session.get(
            CLOUD_CLOCK_LIST_URL,
            params={
                "DeviceId": device_id,
                "StartNum": 1,
                "EndNum": 100,
                "DeviceType": device_type,
            },
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=aiohttp.ClientTimeout(total=15),
        ) as resp:
            data = await resp.json()
    except Exception as exc:
        _LOGGER.error("Failed to fetch cloud clock list: %s", exc)
        return clocks

    if data.get("ReturnCode") != 0:
        _LOGGER.error("Cloud API error: %s", data.get("ReturnMessage"))
        return clocks

    for item in data.get("ClockList", []):
        name = item.get("ClockName")
        clock_id = item.get("ClockId")
        if name and clock_id is not None:
            clocks[name] = int(clock_id)

    return clocks


class DivoomClockSelect(DivoomTimesFrameEntity, SelectEntity):
    """Select entity that changes the active clock face."""

    _attr_translation_key = "clock"
    _attr_icon = "mdi:clock-outline"

    def __init__(self, coordinator, entry, api, clocks: dict[str, int]):
        super().__init__(coordinator, entry)
        self._api = api
        self._clocks = dict(clocks)
        self._attr_unique_id = f"{entry.entry_id}_clock"
        self._sync_current_clock()

    def _sync_current_clock(self) -> None:
        """Make sure the currently active clock is always a selectable option."""
        current_id = self.coordinator.data.get("clock_id")
        if current_id is not None and current_id not in self._clocks.values():
            self._clocks[f"Clock {current_id}"] = current_id
        self._clock_names_by_id = {v: k for k, v in self._clocks.items()}
        self._attr_options = list(self._clocks.keys())

    @property
    def current_option(self) -> str | None:
        current_id = self.coordinator.data.get("clock_id")
        return self._clock_names_by_id.get(current_id)

    async def async_select_option(self, option: str) -> None:
        clock_id = self._clocks.get(option)
        if clock_id is None:
            return
        await self._api.set_clock_select_id(clock_id)
        await self.coordinator.async_request_refresh()
