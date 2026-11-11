"""Button platform for Divoom TimesFrame reboot."""
from __future__ import annotations

from homeassistant.components.button import ButtonEntity
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
        [DivoomRebootButton(data["coordinator"], entry, data["api"])], True
    )


class DivoomRebootButton(DivoomTimesFrameEntity, ButtonEntity):
    """Button that reboots the TimesFrame device."""

    _attr_translation_key = "reboot"
    _attr_device_class = "restart"
    _attr_icon = "mdi:restart"

    def __init__(self, coordinator, entry, api):
        super().__init__(coordinator, entry)
        self._api = api
        self._attr_unique_id = f"{entry.entry_id}_reboot"

    async def async_press(self) -> None:
        await self._api.sys_reboot()
