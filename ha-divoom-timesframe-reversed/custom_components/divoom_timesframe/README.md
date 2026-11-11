# Divoom TimesFrame Home Assistant integration

Custom integration for the Divoom TimesFrame smart frame (and similar Wi-Fi Divoom devices that expose the local `divoom_api` on port 9000).

## Features

- Auto-discovery of devices on the local LAN
- Manual setup by IP address
- Entities per device:
  - **Switch** – screen on/off
  - **Number** – brightness (0-100)
  - **Select** – clock face (populated from Divoom cloud)
  - **Sensor** – device info and current clock ID
  - **Button** – reboot
- Service `divoom_timesframe.send_danmaku` – send scrolling text to the screen

## Installation

Copy the `custom_components/divoom_timesframe` folder into your Home Assistant `config/custom_components/` directory and restart Home Assistant.

## Configuration

Add the integration through **Settings → Devices & services → Add integration → Divoom TimesFrame**.

You can either:

- **Scan network** – the integration scans the `/24` subnet of the interface HA uses for outbound traffic.
- **Enter IP manually** – type the IP address of the frame (default port 9000).

Multiple devices are supported; repeat the flow for each frame. After setup, you can change the IP or port from the integration's **Configure** button without editing files.

## Service

```yaml
service: divoom_timesframe.send_danmaku
data:
  device_id: <DEVICE_ID>
  message: "Hello from Home Assistant!"
  color: "#FF0000"
```

## Notes

- Discovery only works when Home Assistant and the frame are on the same IP subnet (or routed so the scan subnet is correct). If discovery does not find the device, use manual IP entry.
- The clock-face list is fetched from Divoom's cloud API and matched against the locally reported `ClockId`.
