from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN

class UltraMSGConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the config flow for UltraMSG."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step of the config flow."""
        # Attempt to check if UltraMSG is already configured via configuration.yaml
        notify_services = self.hass.services.async_services().get("notify", {})
        if "ultramsg" in notify_services:
            return self.async_abort(reason="UltraMSG is already configured via `configuration.yaml")
        else:
            return self.async_abort(reason="Config is Missing, UltraMSG is configured via `configuration.yaml`.")
    
    @callback
    def async_get_options_flow(self):
        """No options flow."""
        return None
