#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt


# ID of temperature sensor
# found in /sys/bus/w1/devices/
sensorid = "28-3c01f0957d92" 

waterSensorPin = 11

# MQTT configuration
 # URL of MQTT broker
mqttBroker = 'test.mosquitto.org'
# Create the client object and give it a name
client = mqtt.Client('RPi')
# Count alarm publishes
alarm = 0


def main():
    """
    Main method
    """
    global alarm
    # If water is detected, immediately send an alarm
    # Include temperature data with alarm
    while alarm < 1:     
        # Loop every second until water alarm is publish
        if not determineWater():
            # If no water is detected, do nothing
            print(f'Current Temperatue: {readSensor()} F')  
            print('Water Level (Garage): OK\n')
        else:
            # Send an alarm notification if water is detected.
            print('ALARM: WATER DETECTED!\n')
            # First argument is the MQTT topic to publish to
            # Second argument is the body of the published message
            client.publish('ALARM_STATUS', f'Water levels in the garage are above normal.')
            alarm += 1

        time.sleep(1)


def readSensor():
    """
    Reads data from the temperature sensor
    """
    # Open the sensor file and read its values to a variable
    with open("/sys/bus/w1/devices/" + sensorid + "/w1_slave") as f:
        text = f.read()
    # Conversion logic
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temp = float(temperaturedata[2:])
    # Gets temp in celcius
    tempC = temp / 1000
    # Call the conversion method to return degrees in fahrenheit
    return str(getTempF(tempC))


def getTempF(tempC):
    """
    Converts temperature from celcius to fahrenheit
    """
    f = 9 / 5
    tempF = (tempC * f) + 32
    # Round temp to 2 decimal places
    return str(round(tempF, 2))


def determineWater():
    """
    Reads water level sensor and returns a bool
    """
    if(GPIO.input(waterSensorPin)):
        return True
    else:
        return False


def setup():
    """
    Initializes the RPi and connects to MQTT broker
    """
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(waterSensorPin, GPIO.IN)
    # Connect to the MQTT broker
    client.connect(mqttBroker)


def destroy():
    """
    Clean up on exit
    """
    GPIO.cleanup()


if __name__ == '__main__':
    try:
        setup()
        main()
    except KeyboardInterrupt:
        destroy()
