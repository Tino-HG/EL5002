import paho.mqtt.publish as publish
import time
print("Sending 0...")
publish.single("windowsTopic", "0", hostname="localhost")
time.sleep(1)
print("Sending 1...")
publish.single("windowsTopic", "1", hostname="localhost")
