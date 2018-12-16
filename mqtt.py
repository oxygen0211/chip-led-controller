import paho.mqtt.client as mqtt
import json

class MQTT:
    def __init__(self, colorCallback):
        self.colorCallback = colorCallback
        self.on = False

    def on_connect(self, client, userdata, flags, rc):
        print('MQTT Connection established')
        client.subscribe([("livingroom/tv-schrank/switch", 0), ("livingroom/tv-schrank/rgb/command", 0)])
        self.publish_rgb_state(0, 0, 0)

    def on_message(self, client, userdata, msg):
        try:
            config = json.loads(msg.payload)

            if msg.topic == "livingroom/tv-schrank/switch":
                if config["switch"] == True:
                    if self.on != True:
                        if not self.color:
                            self.color = {"red": 255, "blue": 255, "green": 255}
                        print("Switching on lights")
                        self.colorCallback(self.color["red"], self.color["green"], self.color["blue"])
                        self.on = True
                else:
                    print("Switching off lights")
                    self.colorCallback(0, 0, 0)
                    self.on = False

            elif msg.topic == "livingroom/tv-schrank/rgb/command":
                print("Setting lights to r:{}, g:{}, b:{}".format(config["red"], config["green"], config["blue"]))
                self.colorCallback(config["red"], config["green"], config["blue"])
                self.color = config
        except Exception as e:
            print "Error while processing message:"
            print e

    def publish_rgb_state(self, red, green, blue):
        color = "{},{},{}".format(red, green, blue)
        self.client.publish("livingroom/tv-schrank/rgb/state", color)

    def connect(self, broker, user, password):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set(user, password)
        self.client.connect(broker, 1883, 60)
        self.client.loop_forever()
