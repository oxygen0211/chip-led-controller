import CHIP_IO.GPIO as GPIO

class LED_GPIO:
    def __init__(self):
        green = 'XIO-P0'
        blue = 'XIO-P1'
        red = 'XIO-P2'

        self.green = green
        self.red = red
        self.blue = blue

        GPIO.setup(green, GPIO.OUT)
        GPIO.setup(blue, GPIO.OUT)
        GPIO.setup(red, GPIO.OUT)

    def setPin(self, pin, value):
        GPIO.output(pin, value)

    def setRed(self, value):
        self.setPin(self.red, value)

    def setGreen(self, value):
        self.setPin(self.green, value)

    def setBlue(self, value):
        self.setPin(self.blue, value)
