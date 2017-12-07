import CHIP_IO.GPIO as GPIO
import CHIP_IO.SOFTPWM as SPWM

class LED_GPIO:
    def __init__(self):
        green = 'XIO-P0'
        blue = 'XIO-P1'
        red = 'XIO-P2'
        frequency = 100

        self.green = green
        self.red = red
        self.blue = blue

        GPIO.cleanup(red)
        GPIO.cleanup(green)
        GPIO.cleanup(blue)

        SPWM.start(red, 0)
        SPWM.set_frequency(red, frequency)
        SPWM.start(green, 0)
        SPWM.set_frequency(green, frequency)
        SPWM.start(blue, 0)
        SPWM.set_frequency(blue, frequency)

    def setPin(self, pin, value):
        # we assume RGB values from 0 to 255, but SPWM expects 0 to 100,
        # so we have to normalize
        duty = value/2.55
        print('setting value '+str(duty)+' for '+pin)
        SPWM.set_duty_cycle(pin, duty)

    def setRed(self, value):
        self.setPin(self.red, value)

    def setGreen(self, value):
        self.setPin(self.green, value)

    def setBlue(self, value):
        self.setPin(self.blue, value)
