# chip-led-controller

A module for integrating LED lightstrips (or in my case Glass lighting clips by Koch) with a NextThing co. C.H.I.P

## Hardware setup
The wiring is based on [https://dordnung.de/raspberrypi-ledstrip/]. I am using IRLZ34N MOSFETs and an external 12v power source
for transmitting 12v into the LEDs.

This project assumes the following connection between color gates and GPIO ports:
* XIO0 (gpio1013 on Kernel 4.4) -> Green
* XIO1 (gpio1014 on Kernel 4.4) -> Blue
* XIO2 (gpio1015 on Kernel 4.4) -> Red


## Environment setup

```
sudo apt-get update
sudo apt-get install git build-essential python-dev python-pip flex bison chip-dt-overlays -y
```
copy code to /opt/led-controller
```
sudo pip install -r requirements.txt
sudo python main.py
```

## running as a service
copy led-controller.service to /etc/systemd/system/
```
sudo systemctl daemon-reload
sudo service led-controller start
```

## Setting colors
```
curl -XPOST -H "Content-Type: application/json" --data '{"red": 255, "blue": 255, "green": 255}' http://chip-led.local:5000/
```
