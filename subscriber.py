import time
from config import *
import paho.mqtt.client as mqtt

MQTT_SERVER = mqtt_config['server']
MQTT_PATH = mqtt_config['topic']

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_PATH)

def on_message(client, userdata, msg):
    # generate filename
    timestamp = time.gmtime()
    time_str = '%4d%02d%02d%02d%02d%02d' %(timestamp[0], timestamp[1], timestamp[2], timestamp[4], timestamp[5], timestamp[6])
    # Create a file with write byte permission
    f = open('photos/'+time_str+'.jpg', "wb")
    f.write(msg.payload)
    f.close()
    print("Image received and saved!")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()