"""Switch platform for Divoom TimesFrame screen on/off."""
from __future__ import annotations

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .entity import DivoomTimesFrameEntity


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    data = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        [DivoomScreenSwitch(data["coordinator"], entry, data["api"])], True
    )


class DivoomScreenSwitch(DivoomTimesFrameEntity, SwitchEntity):
    """Switch that turns the TimesFrame screen on and off."""

    _attr_translation_key = "screen"
    _attr_icon = "mdi:monitor"

    def __init__(self, coordinator, entry, api):
        super().__init__(coordinator, entry)
        self._api = api
        self._attr_unique_id = f"{entry.entry_id}_screen"

    @property
    def is_on(self) -> bool:
        return bool(self.coordinator.data.get("screen_on"))

    async def async_turn_on(self, **kwargs) -> None:
        await self._api.set_on_off_screen(True)
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs) -> None:
        await self._api.set_on_off_screen(False)
        await self.coordinator.async_request_refresh()
