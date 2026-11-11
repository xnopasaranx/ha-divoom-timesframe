"""Base entity for Divoom TimesFrame."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import CONF_DEVICE_ID, CONF_DEVICE_TYPE, CONF_NAME, DOMAIN
from .coordinator import DivoomTimesFrameCoordinator


class DivoomTimesFrameEntity(CoordinatorEntity):
    """Base entity for a TimesFrame device."""

    _attr_has_entity_name = True

    def __init__(
        self, coordinator: DivoomTimesFrameCoordinator, entry: ConfigEntry
    ) -> None:
        super().__init__(coordinator)
        self._entry = entry
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(entry.data[CONF_DEVICE_ID]))},
            name=entry.data.get(CONF_NAME, "Divoom TimesFrame"),
            manufacturer="Divoom",
            model="TimesFrame",
            sw_version=entry.data.get(CONF_DEVICE_TYPE, "Frame"),
        )
