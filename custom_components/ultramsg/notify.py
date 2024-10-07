# custom_components/ultramsg/notify.py

from .const import DOMAIN
from homeassistant.components.notify import BaseNotificationService
import logging

_LOGGER = logging.getLogger(__name__)

CONF_INSTANCE_ID = "instance_id"
CONF_TOKEN = "token"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_INSTANCE_ID): cv.string,
    vol.Required(CONF_TOKEN): cv.string,
})

def get_service(hass, config, discovery_info=None):
    """Get the UltraMSG notification service."""
    instance_id = config.get(CONF_INSTANCE_ID)
    token = config.get(CONF_TOKEN)
    
    if instance_id and token:
        hass.data.setdefault(DOMAIN, {})
        hass.data[DOMAIN]['configured'] = True
        return UltraMSGNotificationService(instance_id, token)
    else:
        _LOGGER.error("UltraMSG configuration incomplete.")
        hass.data.setdefault(DOMAIN, {})
        hass.data[DOMAIN]['configured'] = False
        return None

class UltraMSGNotificationService(BaseNotificationService):
    """Implement the notification service for UltraMSG."""

    def __init__(self, instance_id, token):
        """Initialize the service."""
        self.instance_id = instance_id
        self.token = token
        self.api_url = f"https://api.ultramsg.com/{self.instance_id}/messages/chat"

    def send_message(self, message="", **kwargs):
        """Send message to specified target phone number."""
        targets = kwargs.get(ATTR_TARGET)
        data = kwargs.get(ATTR_DATA) or {}

        if not targets:
            _LOGGER.error("No target specified.")
            return

        for target in targets:
            self._send_ultramsg_message(target, message, data)

    def _send_ultramsg_message(self, to, body, data):
        """Send a message via UltraMSG."""
        payload = {
            "token": self.token,
            "to": to,
            "body": body,
            "priority": data.get("priority", 10),
            "referenceId": data.get("referenceId", "HomeAssistant"),
            "msgId": data.get("msgId", ""),
            "mentions": data.get("mentions", ""),
        }

        headers = {
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(self.api_url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            _LOGGER.debug("Message sent to %s: %s", to, body)
        except requests.exceptions.HTTPError as errh:
            _LOGGER.error("HTTP Error: %s", errh)
        except requests.exceptions.ConnectionError as errc:
            _LOGGER.error("Error Connecting: %s", errc)
        except requests.exceptions.Timeout as errt:
            _LOGGER.error("Timeout Error: %s", errt)
        except requests.exceptions.RequestException as err:
            _LOGGER.error("Error: %s", err)
