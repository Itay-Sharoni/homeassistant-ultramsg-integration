"""The UltraMsg integration."""
import logging

import voluptuous as vol

from homeassistant.const import CONF_TOKEN
from homeassistant.core import HomeAssistant
from homeassistant.helpers import discovery
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN, CONF_INSTANCE_ID

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_INSTANCE_ID): str,
                vol.Required(CONF_TOKEN): str,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the UltraMsg integration."""
    hass.data.setdefault(DOMAIN, {})

    if DOMAIN in config:
        hass.data[DOMAIN] = config[DOMAIN]
        await discovery.async_load_platform(hass, "notify", DOMAIN, {}, config)

    return True

async def async_setup_entry(hass: HomeAssistant, entry):
    """Set up UltraMsg from a config entry."""
    hass.data[DOMAIN][entry.entry_id] = entry.data
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "notify")
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry):
    """Unload an UltraMsg config entry."""
    await hass.config_entries.async_forward_entry_unload(entry, "notify")
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
