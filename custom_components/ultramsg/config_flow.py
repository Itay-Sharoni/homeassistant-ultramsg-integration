from homeassistant import config_entries
from homeassistant.core import callback

class UltraMSGConfigFlow(config_entries.ConfigFlow, domain='ultramsg'):
    """Handle a config flow for UltraMSG."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        return self.async_abort(reason="not_needed")

    @callback
    def async_get_options_flow(self):
        """No options flow."""
        return None
