from client import LEDStrip

led = LEDStrip('chip-led.local', 5000)
success = led.setColor(255, 0, 0)
print success
