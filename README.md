## Configuration via `configuration.yaml`

You can configure the integration using `configuration.yaml` instead of the UI.

```yaml
# configuration.yaml
ultramsg:
  instance_id: YOUR_INSTANCE_ID
  token: YOUR_TOKEN

notify:
  - platform: ultramsg
    name: ultramsg
