# homeassistant-ultramsg-integration

Send Home Assistant notifications to WhatsApp using UltraMSG.

## Installation

1. **Copy** the `custom_components/ultramsg` directory into your Home Assistant's `config/custom_components/` directory.

2. **Create** a new notification service in your `configuration.yaml` file:

   ```yaml
   notify:
     - name: send_ultramsg
       platform: ultramsg
       instance_id: "<your UltraMSG instance ID>"
       token: "<your UltraMSG token>"
