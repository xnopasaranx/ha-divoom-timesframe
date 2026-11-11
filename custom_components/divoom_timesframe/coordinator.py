"""DataUpdateCoordinator for Divoom TimesFrame."""
from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import DivoomTimesFrameApi
from .const import DOMAIN, UPDATE_INTERVAL

_LOGGER = logging.getLogger(__name__)


class DivoomTimesFrameCoordinator(DataUpdateCoordinator):
    """Coordinator that fetches the current state of a TimesFrame device."""

    def __init__(self, hass: HomeAssistant, api: DivoomTimesFrameApi) -> None:
        self.api = api
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=UPDATE_INTERVAL),
        )

    async def _async_update_data(self) -> dict:
        try:
            screen = await self.api.get_on_off_screen()
            clock = await self.api.get_clock_info()
        except Exception as exc:
            raise UpdateFailed(f"Failed to update TimesFrame data: {exc}") from exc

        return {
            "screen_on": screen.get("OnOff") == 1,
            "brightness": clock.get("Brightness"),
            "clock_id": clock.get("ClockId"),
            "device_id": screen.get("DeviceId"),
            "device_type": screen.get("DeviceType"),
        }
