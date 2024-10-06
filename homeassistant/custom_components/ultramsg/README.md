# UltraMsg Home Assistant Integration

This custom component allows you to send WhatsApp messages via the UltraMsg service using Home Assistant.

## Installation

1. **Install via HACS**:
   - Add this repository to HACS as a custom repository.
   - Install the "UltraMsg" integration.

2. **Manual Installation**:
   - Copy the `ultramsg` folder to your `custom_components` directory.

## Configuration

1. **Restart Home Assistant** after installation.

2. **Configure the integration via the UI**:
   - Go to **Configuration** > **Devices & Services**.
   - Click **Add Integration**.
   - Search for **UltraMsg**.
   - Enter your **Instance ID** and **Token**.

## Usage

Use the `notify.ultramsg` service to send messages.

### Example Service Call

```yaml
service: notify.ultramsg
data:
  message: "Hello from Home Assistant!"
  target:
    - "+1234567890"
