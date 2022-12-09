#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt


# ID of temperature sensor
# found in /sys/bus/w1/devices/
sensorid = "28-3c01f0957d92" 

waterSensorPin = 11

# MQTT configuration
mqttBroker = 'test.mosquitto.org' # URL of MQTT broker
client = mqtt.Client('RPi') # Create the client object and give it a name


def main():
    while True:
        print(f'Current Temperatue: {readSensor()}')
        if not determineWater():
            print('Water Level: OK\n')
        else:
            # Send an alarm notification if water is detected.
            print('ALARM: WATER DETECTED!\n')
            #client.publish('Water Status', "ALARM: WATER DETECTED!")

        time.sleep(5)


# Read data from the temperature sensor
def readSensor():
    with open("/sys/bus/w1/devices/" + sensorid + "/w1_slave") as tfile:
        text = tfile.read()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temp = float(temperaturedata[2:])
    tempC = temp / 1000
    return str(getTempF(tempC))


# Convert temperature from celcius to fahrenheit
def getTempF(tempC):
    f = 9 / 5
    tempF = (tempC * f) + 32
    return tempF

# Reads water level sensor
def determineWater():
    if(GPIO.input(waterSensorPin)):
        return True
    else:
        return False


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(waterSensorPin, GPIO.IN)
    # Connect to the MQTT broker
    client.connect(mqttBroker)


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    try:
        setup()
        main()
    except KeyboardInterrupt:
        destroy()
