# ITD-3223 Class Project Pt. 2

## Description

This project demonstrates an end-to-end IoT solution by reading sensor data and publishing to an MQTT broker.
The reading and publishing of sensor data is facilitated through use of a Raspberry Pi running Node-RED and Python.
The purpose of this project is to simulate a flood-detection alarm, as well as provide temperature data.

## Physical Setup

![Wiring Diagram](https://awilmes-github-artifacts.s3.amazonaws.com/itd-3223-class-proj-part-2/class_proj_part2.drawio.png "RPi GPIO Wiring Diagram")

## Installation Instructions

**Prerequisites**

Raspberry Pi:
- Node-RED

Smartphone:
- Remote-RED app (for push notifications)

Python (3.9.2^):
- RPi.GPIO
- paho-mqtt

**Install Node-RED**

1. From the Raspberry Pi CLI run:

> `bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)`

2. Start Node-RED:

> `node-red-start`

3. Open the Node-RED UI from a web browser on the same network:

> `<RPi IP>:1880`

4. From the Node-RED UI, use "Manage Palette" to install the following packages:
    - > `node-red-contrib-remote` (Adds remote function blocks for configuring push notifications)
    - > `node-red-node-email` (Adds social blocks for email access)

4. To stop the Node-RED service, run:

> `node-red-stop`

**Configure RPi Python Environment**

1. Create a virtual environment in the project root directory:

> `python -m venv .venv`

2. Activate the virtual environment:

(macOS) > `source .venv/bin/activate`

(Windows) > `.venv\Scripts\activate.bat`

3. Install dependencies:

> `pip install requirements.txt`

**Configure Node-RED Flow**

![Node-RED Flow](https://awilmes-github-artifacts.s3.amazonaws.com/itd-3223-class-proj-part-2/node-red-flow.png "Node-RED Flow")

1. remote-access node:
    - Connect your flow to the Remote-RED app by following the documentation [here](https://www.remote-red.com/en/help/).

2. mqtt in node:
    - Configure a server and select it
    - Enter the topic to subscribe to ('ALARM_STATUS' for this project)

3. debug node (output):
    - Shows output in local UI
    - Not required but useful for troubleshooting

4. remote-notification node
    - Select the config you made for the remote-access node
    - Add a title for the message (string)
    - Add a body for the message (msg.payload)

5. email node:
    - Note: Requires a gmail account with 2FA enabled. This allows you to create an app password for use with this node.

