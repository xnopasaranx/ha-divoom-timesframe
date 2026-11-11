"""Sensor platform for Divoom TimesFrame device info."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
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
        [
            DivoomDeviceInfoSensor(data["coordinator"], entry),
            DivoomClockIdSensor(data["coordinator"], entry),
        ],
        True,
    )


class DivoomDeviceInfoSensor(DivoomTimesFrameEntity, SensorEntity):
    """Sensor reporting the device ID and type."""

    _attr_translation_key = "device_info"
    _attr_icon = "mdi:information-outline"

    def __init__(self, coordinator, entry):
        super().__init__(coordinator, entry)
        self._attr_unique_id = f"{entry.entry_id}_device_info"

    @property
    def native_value(self) -> str:
        return f"{self.coordinator.data.get('device_type')} {self.coordinator.data.get('device_id')}"


class DivoomClockIdSensor(DivoomTimesFrameEntity, SensorEntity):
    """Sensor reporting the currently active clock ID."""

    _attr_translation_key = "clock_id"
    _attr_icon = "mdi:identifier"

    def __init__(self, coordinator, entry):
        super().__init__(coordinator, entry)
        self._attr_unique_id = f"{entry.entry_id}_clock_id"

    @property
    def native_value(self) -> int | None:
        return self.coordinator.data.get("clock_id")
