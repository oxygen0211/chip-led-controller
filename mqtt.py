import paho.mqtt.client as mqtt
import json

class MQTT:
    def __init__(self, colorCallback):
        self.colorCallback = colorCallback

    def on_connect(self, client, userdata, flags, rc):
        print('MQTT Connection established')
        client.subscribe([("livingroom/tv-schrank/switch", 0), ("livingroom/tv-schrank/rgb/command", 0)])
        self.publish_rgb_state(0, 0, 0)

    def on_message(self, client, userdata, msg):
        try:
            config = json.loads(msg.payload)

            if msg.topic == "livingroom/tv-schrank/switch":
                if config["switch"] == True:
                    print("Switching on lights")
                    self.colorCallback(255, 255, 255)
                else:
                    print("Switching off lights")
                    self.colorCallback(0, 0, 0)

            elif msg.topic == "livingroom/tv-schrank/rgb/command":
                print("Setting lights to r:{}, g:{}, b:{}".format(config["red"], config["green"], config["blue"]))
                self.colorCallback(config["red"], config["green"], config["blue"])
        except Exception as e:
            print "Error while processing message:"
            print e

    def publish_rgb_state(self, red, green, blue):
        color = "{},{},{}".format(red, green, blue)
        self.client.publish("livingroom/tv-schrank/rgb/state", color)

    def connect(self, broker):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker, 1883, 60)
        self.client.loop_forever()
