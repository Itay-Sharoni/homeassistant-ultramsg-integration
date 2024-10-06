# UltraMsg Home Assistant Integration

This custom component allows you to send WhatsApp messages via the UltraMsg service using Home Assistant.

## Installation

### HACS Installation

1. **Add** this repository to HACS as a custom repository:
   - In Home Assistant, go to **HACS** > **Integrations**.
   - Click the three dots in the top right corner and select **"Custom repositories"**.
   - Enter the repository URL: `https://github.com/Itay-Sharoni/HomeAssistant_UltraMSG`
   - Select **Integration** as the category.
   - Click **Add**.

2. **Install** the integration:
   - Go back to **HACS** > **Integrations**.
   - Click **"Explore & Download Repositories"**.
   - Search for **UltraMsg**.
   - Click **"Download"** to install.

3. **Restart Home Assistant** after installation.

### Manual Installation (Alternative)

1. **Download** the `ultramsg` directory from the `custom_components` folder in this repository.

2. **Copy** the `ultramsg` directory into your Home Assistant's `custom_components` directory.

3. **Restart Home Assistant** after installation.

## Configuration

1. **Restart Home Assistant** if you haven't already.

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
    - "+1234567890"  # Replace with the recipient's phone number
