# custom_components/ultramsg/config_flow.py

from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN

class UltraMSGConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the config flow for UltraMSG."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step of the config flow."""
        return self.async_abort(reason="ui_not_required")

    @callback
    def async_get_options_flow(self):
        """No options flow."""
        return None
