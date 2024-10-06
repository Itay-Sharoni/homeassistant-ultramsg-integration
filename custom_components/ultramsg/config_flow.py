"""Config flow for UltraMsg integration."""
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_TOKEN

from .const import DOMAIN, CONF_INSTANCE_ID

class UltraMsgConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for UltraMsg."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            # Here you could add validation of user input
            await self.async_set_unique_id(user_input[CONF_INSTANCE_ID])
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title="UltraMsg", data=user_input)

        data_schema = vol.Schema({
            vol.Required(CONF_INSTANCE_ID): str,
            vol.Required(CONF_TOKEN): str,
        })

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )
