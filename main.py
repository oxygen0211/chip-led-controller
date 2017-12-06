from gpiocontrol import LED_GPIO
from flask import Flask
from flask import request
import time
import json

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

    led.setRed(red)
    led.setGreen(green)
    led.setBlue(blue)

    return str(red)+", "+str(green)+", "+str(blue)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
