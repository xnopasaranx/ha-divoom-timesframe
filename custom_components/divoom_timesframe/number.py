"""Number platform for Divoom TimesFrame brightness."""
from __future__ import annotations

from homeassistant.components.number import NumberEntity, NumberMode
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
        [DivoomBrightnessNumber(data["coordinator"], entry, data["api"])], True
    )


class DivoomBrightnessNumber(DivoomTimesFrameEntity, NumberEntity):
    """Number entity to control screen brightness."""

    _attr_translation_key = "brightness"
    _attr_icon = "mdi:brightness-6"
    _attr_native_min_value = 0
    _attr_native_max_value = 100
    _attr_native_step = 1
    _attr_native_unit_of_measurement = "%"
    _attr_mode = NumberMode.SLIDER

    def __init__(self, coordinator, entry, api):
        super().__init__(coordinator, entry)
        self._api = api
        self._attr_unique_id = f"{entry.entry_id}_brightness"

    @property
    def native_value(self) -> int | None:
        return self.coordinator.data.get("brightness")

    async def async_set_native_value(self, value: float) -> None:
        await self._api.set_brightness(int(value))
        await self.coordinator.async_request_refresh()
