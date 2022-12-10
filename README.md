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
- Remote-RED (for push notifications)

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

4. To stop the Node-RED service, run:

> `node-red-stop`

## Screenshots

**Node-RED**

TODO: Add Screenshots
