"""Config flow for Divoom TimesFrame integration."""
from __future__ import annotations

import logging
from typing import Any

import aiohttp
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_NAME, CONF_PORT
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import DivoomTimesFrameApi
from .const import (
    CONF_DEVICE_ID,
    CONF_DEVICE_TYPE,
    DEFAULT_PORT,
    DOMAIN,
)
from .discovery import async_discover_devices

_LOGGER = logging.getLogger(__name__)


class DivoomTimesFrameConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Divoom TimesFrame."""

    VERSION = 1

    def __init__(self) -> None:
        self._discovered: dict[int, dict[str, Any]] = {}

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> DivoomTimesFrameOptionsFlow:
        """Return the options flow."""
        return DivoomTimesFrameOptionsFlow(config_entry)

    @callback
    def _device_name(self, device: dict[str, Any]) -> str:
        return f"{device['name']} ({device['host']})"

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        return self.async_show_menu(
            step_id="user",
            menu_options=["scan", "manual"],
        )

    async def async_step_scan(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        errors: dict[str, str] = {}

        if user_input is not None:
            device = self._discovered[user_input["device"]]
            await self.async_set_unique_id(str(device["device_id"]))
            self._abort_if_unique_id_configured()
            return self.async_create_entry(
                title=device["name"],
                data={
                    CONF_HOST: device["host"],
                    CONF_PORT: DEFAULT_PORT,
                    CONF_NAME: device["name"],
                    CONF_DEVICE_ID: device["device_id"],
                    CONF_DEVICE_TYPE: device["device_type"],
                },
            )

        session = async_get_clientsession(self.hass)
        self._discovered = await async_discover_devices(session)

        if not self._discovered:
            return self.async_show_form(
                step_id="manual",
                errors={"base": "no_devices_found"},
            )

        options = {
            device_id: self._device_name(device)
            for device_id, device in self._discovered.items()
        }

        return self.async_show_form(
            step_id="scan",
            data_schema=vol.Schema(
                {vol.Required("device"): vol.In(options)}
            ),
            errors=errors,
        )

    async def async_step_manual(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        errors: dict[str, str] = {}

        if user_input is not None:
            host = user_input[CONF_HOST]
            port = user_input.get(CONF_PORT, DEFAULT_PORT)
            name = user_input.get(CONF_NAME, f"TimesFrame ({host})")
            session = async_get_clientsession(self.hass)
            api = DivoomTimesFrameApi(host, port, session)

            try:
                info = await api.probe()
            except aiohttp.ClientError as exc:
                _LOGGER.error("Cannot connect to %s:%s: %s", host, port, exc)
                errors["base"] = "cannot_connect"
            except Exception as exc:
                _LOGGER.exception("Unexpected error during manual setup: %s", exc)
                errors["base"] = "unknown"
            else:
                device_id = info.get("device_id")
                if not device_id:
                    errors["base"] = "cannot_connect"
                else:
                    await self.async_set_unique_id(str(device_id))
                    self._abort_if_unique_id_configured()
                    return self.async_create_entry(
                        title=name,
                        data={
                            CONF_HOST: host,
                            CONF_PORT: port,
                            CONF_NAME: name,
                            CONF_DEVICE_ID: device_id,
                            CONF_DEVICE_TYPE: info.get("device_type", "Frame"),
                        },
                    )

        return self.async_show_form(
            step_id="manual",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_HOST): str,
                    vol.Optional(CONF_PORT, default=DEFAULT_PORT): int,
                    vol.Optional(CONF_NAME, default=f"TimesFrame"): str,
                }
            ),
            errors=errors,
        )


class DivoomTimesFrameOptionsFlow(config_entries.OptionsFlow):
    """Handle options flow for Divoom TimesFrame."""

    def __init__(self, entry: config_entries.ConfigEntry) -> None:
        self.entry = entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        errors: dict[str, str] = {}

        if user_input is not None:
            host = user_input[CONF_HOST]
            port = user_input.get(CONF_PORT, DEFAULT_PORT)
            session = async_get_clientsession(self.hass)
            api = DivoomTimesFrameApi(host, port, session)

            try:
                info = await api.probe()
            except aiohttp.ClientError as exc:
                _LOGGER.error("Cannot connect to %s:%s: %s", host, port, exc)
                errors["base"] = "cannot_connect"
            except Exception as exc:
                _LOGGER.exception("Unexpected error during options flow: %s", exc)
                errors["base"] = "unknown"
            else:
                device_id = info.get("device_id")
                if not device_id or device_id != self.entry.data.get(CONF_DEVICE_ID):
                    errors["base"] = "wrong_device"
                else:
                    self.hass.config_entries.async_update_entry(
                        self.entry,
                        data={**self.entry.data, CONF_HOST: host, CONF_PORT: port},
                    )
                    return self.async_create_entry(title="", data={})

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_HOST, default=self.entry.data.get(CONF_HOST)
                    ): str,
                    vol.Optional(
                        CONF_PORT, default=self.entry.data.get(CONF_PORT, DEFAULT_PORT)
                    ): int,
                }
            ),
            errors=errors,
        )
