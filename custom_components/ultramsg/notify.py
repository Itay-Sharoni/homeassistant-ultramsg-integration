"""UltraMsg platform for notify component."""
import logging
import aiohttp

from homeassistant.components.notify import (
    BaseNotificationService,
    ATTR_TARGET,
    ATTR_DATA,
)
from homeassistant.const import CONF_TOKEN
from homeassistant.core import HomeAssistant

from .const import DOMAIN, CONF_INSTANCE_ID

_LOGGER = logging.getLogger(__name__)

async def async_get_service(hass: HomeAssistant, config, discovery_info=None):
    """Get the UltraMsg notification service."""
    if discovery_info is None:
        # YAML configuration
        instance_id = hass.data[DOMAIN].get(CONF_INSTANCE_ID)
        token = hass.data[DOMAIN].get(CONF_TOKEN)
    else:
        # UI configuration
        entry_id = discovery_info["entry_id"]
        entry_data = hass.data[DOMAIN].get(entry_id)
        if not entry_data:
            _LOGGER.error("No configuration data found for UltraMsg")
            return None
        instance_id = entry_data.get(CONF_INSTANCE_ID)
        token = entry_data.get(CONF_TOKEN)

    if not instance_id or not token:
        _LOGGER.error("Instance ID and Token must be set")
        return None

    return UltraMsgNotificationService(instance_id, token)

class UltraMsgNotificationService(BaseNotificationService):
    """Implementation of the notification service for UltraMsg."""

    def __init__(self, instance_id: str, token: str):
        """Initialize the service."""
        self._instance_id = instance_id
        self._token = token
        self._api_url = f"https://api.ultramsg.com/{instance_id}/messages/chat"

    async def async_send_message(self, message: str = "", **kwargs):
        """Send a message to specified target(s)."""
        targets = kwargs.get(ATTR_TARGET)
        data = kwargs.get(ATTR_DATA) or {}

        if not targets:
            _LOGGER.error("No target specified")
            return

        async with aiohttp.ClientSession() as session:
            for target in targets:
                payload = {
                    "token": self._token,
                    "to": target,
                    "body": message,
                    "priority": data.get("priority", 10),
                    "referenceId": data.get("referenceId", ""),
                    "msgId": data.get("msgId", ""),
                    "mentions": data.get("mentions", ""),
                }

                try:
                    async with session.post(self._api_url, json=payload, timeout=10) as response:
                        response.raise_for_status()
                        _LOGGER.debug("Message sent to %s: %s", target, message)
                except aiohttp.ClientError as e:
                    _LOGGER.error("Error sending message to %s: %s", target, e)
