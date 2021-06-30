# Ratchet_Button Test Client
import sys
import ssl
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time
import random

mqttc = AWSIoTMQTTClient("SmartParkingDevice1")

# Make sure you use your GGC end-point!!
mqttc.configureEndpoint("greengrass-ats.iot.us-west-2.amazonaws.com",8883)
mqttc.configureCredentials("./root.ca.pem","./private.key","./cert.pem")

#Function to encode a payload into JSON
def json_encode(string):
    return json.dumps(string)

mqttc.json_encode=json_encode


counter=0

while True:
  
  message = {
    "timestamp": time.time(),
	"metrics": [
		 {
			"name": "sp-area1-sensor1/BatteryLife",
			"value": 95
		 },
		 {
			"name": "sp-area1-sensor1/IsOccupied",
			"value": 1
		 },
		 {
			"name": "sp-area1-sensor1/reason",
			"value": 'Not Available'
		 }
	]
  }

  #Encoding into JSON
  message = mqttc.json_encode(message)

  mqttc.connect()

  print "Connected to the Greengrass core!"

  mqttc.publish("spBv1.0/state1/DDATA/city1/area1", message, 0)


  print "Message Published"

  mqttc.disconnect()

  time.sleep(100)





