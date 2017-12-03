from gpiocontrol import LED_GPIO
import time

led = LED_GPIO()

led.setRed(0)
led.setBlue(0)
led.setGreen(0)

while True:
    led.setRed(1)
    time.sleep(1)
    led.setBlue(1)
    led.setRed(0)
    time.sleep(1)
    led.setBlue(0)
    led.setGreen(1)
    time.sleep(1)
    led.setGreen(0)
