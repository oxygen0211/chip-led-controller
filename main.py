from gpiocontrol import LED_GPIO
from mqtt import MQTT
from flask import Flask
from flask import request
import time
import json
import os

led = LED_GPIO()

led.setRed(0)
led.setBlue(0)
led.setGreen(0)

app = Flask(__name__)

@app.route("/", methods=["POST"])
def setLight():
    data = request.get_json()
    red = int(data["red"])
    blue = int(data["blue"])
    green = int(data["green"])

    setLightValues(red, gree, blue)

    return str(red)+", "+str(green)+", "+str(blue)

def setLightValues(red, green, blue):
    led.setRed(red)
    led.setGreen(green)
    led.setBlue(blue)
    mqtt.publish_rgb_state(red, green, blue)

mqtt = MQTT(setLightValues)

if __name__ == "__main__":
    mqttBroker = os.environ.get("MQTT_BROKER")
    mqttUser = os.environ.get("MQTT_USER")
    mqttPass = os.environ.get("MQTT_PASSWORD")
    if(mqttBroker == None):
        print("No MQTT broker set, starting in HTTP mode")
        app.run(host='0.0.0.0')
    else:
        mqtt.connect(mqttBroker, mqttUser, mqttPass)
