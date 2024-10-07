# Home Assistant UltraMSG Integration

![HACS](https://img.shields.io/badge/HACS-Custom-blue)
![License](https://img.shields.io/github/license/Itay-Sharoni/homeassistant-ultramsg-integration)
[![Github Downloads (total)](https://img.shields.io/github/downloads/Itay-Sharoni/homeassistant-ultramsg-integration/total.svg)]()
![Stars](https://img.shields.io/github/stars/Itay-Sharoni/homeassistant-ultramsg-integration?style=social)


Send Home Assistant notifications directly to WhatsApp using **UltraMSG** with this seamless integration!


# Clarification
**This integration solely utilizes the UltraMSG service for sending notifications and is not affiliated with, endorsed by, or related to WhatsApp or Meta in any way.**

## 📖 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Install via HACS](#install-via-hacs)
  - [Manual Installation](#manual-installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🌟Features

- **Instant Notifications**: Receive real-time alerts on WhatsApp for various Home Assistant events.
- **Easy Setup**: Simple configuration with clear instructions.
- **Customizable**: Tailor notifications to suit your specific needs.
- **Secure**: Utilizes UltraMSG’s secure messaging platform.

## 🛠Prerequisites

Before you begin, ensure you have the following:

- **Home Assistant**: Running on your preferred hardware.
- **HACS (Home Assistant Community Store)**: Installed and configured. If you haven't set up HACS yet, follow the [official HACS installation guide](https://hacs.xyz/docs/installation/prerequisites).
- **UltraMSG Account**: Sign up at [UltraMSG](https://www.ultramsg.com/) to obtain your `Instance ID` and `Token`.

## 📥Installation

### Install via HACS

1. **Open Home Assistant** and navigate to **HACS** in the sidebar.

2. Click on **Integrations**.

3. Click the **+** button in the bottom right corner to add a new integration.

4. Enter the repository URL:

5. Select **Home Assistant UltraMSG Integration** from the list.

6. Click **Install** and follow any on-screen prompts.

7. **Restart Home Assistant** to complete the installation.

### Manual Installation

If you prefer manual installation, follow these steps:

1. **Download the Repository**:

```bash
git clone https://github.com/Itay-Sharoni/homeassistant-ultramsg-integration.git
```
2. **Copy the Integration Files:**
   
   Copy the `custom_components/ultramsg` directory into your Home Assistant's `config/custom_components/` directory.

3. **Restart Home Assistant to recognize the new integration.**



## 🔧Configuration
1. Open your `configuration.yaml` file in the Home Assistant configuration directory.

2. **Add the UltraMSG Notification Service:**
```yaml
notify:
  - name: send_ultramsg
    platform: ultramsg
    instance_id: "<your UltraMSG instance ID>"
    token: "<your UltraMSG token>"
```

Replace `<your UltraMSG instance ID>` and `<your UltraMSG token>` with the credentials obtained from your UltraMSG Dashboard.

3. **Save the Configuration and restart Home Assistant** to apply the changes.
* **Click [here](https://youtu.be/SWkZMCCEQk0?si=pI4rxqxqpqojaGlu&t=51) for a quick guide on configuring configuration.yaml** - credit to [Siytek](https://www.youtube.com/@siytek) for this video

## 🚀Usage

After installation and configuration, you can use the `send_ultramsg` service to send WhatsApp notifications. Here's how to set it up in an automation:

1. **Navigate to Automations** in Home Assistant.
2. **Create a New Automation** or **Edit an Existing One.**
3. **Add an Action** with the following service:
```yaml
service: notify.send_ultramsg
data:
  message: "Hello from Home Assistant!"
  target: "<recipient WhatsApp number>"
```

Replace `<recipient WhatsApp number>` with the desired recipient's number in international format (e.g., `+1234567890`).

## 🐞Troubleshooting

* **No Notifications Received:**
   * Verify that your `instance_id` and `token` are correct.
   * Check the UltraMSG dashboard for any usage limits or errors.
   * Ensure that the recipient number is correctly formatted.
* **Integration Not Showing in HACS:**
   * Make sure you've added the correct repository URL to HACS.
   * Verify that the repository is public and accessible.
* **Check Logs:**
   * Navigate to Configuration > Logs in Home Assistant to view any error messages related to UltraMSG.

 ## 🤝Contributing
 Contributions are welcome! If you'd like to contribute to this integration:

 1. Fork the Repository: [homeassistant-ultramsg-integration]([https://github.com/Itay-Sharoni/homeassistant-ultramsg-integration](https://github.com/Itay-Sharoni/homeassistant-ultramsg-integration.git))
 2. **Create a Feature Branch:**
```bash
git checkout -b feature/YourFeature
```
3. **Commit Your Changes:**
```bash
git commit -m "Add some feature"
```
4. **Push to the Branch:**
```bash
git push origin feature/YourFeature
```
5. **Open a Pull Request describing your changes.**

## 📄License
This project is licensed under the MIT [License](https://github.com/Itay-Sharoni/homeassistant-ultramsg-integration/blob/main/LICENSE).
