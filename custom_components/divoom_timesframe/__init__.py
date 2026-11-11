"""The Divoom TimesFrame integration."""
from __future__ import annotations

import logging

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_PORT
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import DivoomTimesFrameApi
from .const import CONF_DEVICE_ID, DOMAIN
from .coordinator import DivoomTimesFrameCoordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["switch", "number", "select", "sensor", "button"]

SERVICE_SEND_DANMAKU = "send_danmaku"

SEND_DANMAKU_SCHEMA = vol.Schema(
    {
        vol.Required("device_id"): vol.Coerce(int),
        vol.Required("message"): str,
        vol.Optional("color", default="#FFFFFF"): str,
    }
)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Divoom TimesFrame from a config entry."""
    session = async_get_clientsession(hass)
    api = DivoomTimesFrameApi(
        host=entry.data[CONF_HOST],
        port=entry.data[CONF_PORT],
        session=session,
    )

    coordinator = DivoomTimesFrameCoordinator(hass, api)
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "coordinator": coordinator,
        "entry": entry,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Register the send_danmaku service only once.
    if not hass.services.has_service(DOMAIN, SERVICE_SEND_DANMAKU):
        async def async_handle_send_danmaku(call: ServiceCall) -> None:
            device_id = call.data["device_id"]
            message = call.data["message"]
            color = call.data["color"]
            for data in hass.data[DOMAIN].values():
                if data["entry"].data[CONF_DEVICE_ID] == device_id:
                    await data["api"].send_danmaku(message, color)
                    return
            _LOGGER.error("TimesFrame device %s not found", device_id)

        hass.services.async_register(
            DOMAIN,
            SERVICE_SEND_DANMAKU,
            async_handle_send_danmaku,
            schema=SEND_DANMAKU_SCHEMA,
        )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    # If no entries remain, remove the service.
    if unload_ok and not hass.data[DOMAIN]:
        hass.services.async_remove(DOMAIN, SERVICE_SEND_DANMAKU)

    return unload_ok
