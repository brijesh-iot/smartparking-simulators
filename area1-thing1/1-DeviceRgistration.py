import sys
import ssl
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time
import random

mqttc = AWSIoTMQTTClient("smartparking_EdgeGatewayDevice")

#mqttc.configureEndpoint("greengrass-ats.iot.us-west-2.amazonaws.com",8883)
mqttc.configureEndpoint("greengrass-ats.iot.us-east-1.amazonaws.com",8883)
mqttc.configureCredentials("./root.ca.pem","./private.key","./cert.pem")

#Function to encode a payload into JSON
def json_encode(string):
    return json.dumps(string)

mqttc.json_encode=json_encode


counter=0

#while True:
for x in range(1, 2):
  
  message = {
    'timestamp': time.time(),
	'metrics': [
		 {
			'name': 'sp-area1-sensor%s/BatteryLife' %(x),
			'value': '100%'
		 },
		 {
			'name': 'sp-area1-sensor%s/IsOccupied' %(x),
			'value': 0
		 }
	]
  }

  #Encoding into JSON
  message = mqttc.json_encode(message)

  mqttc.connect()

  print "Connected to the Greengrass core!"

  mqttc.publish("spBv1.0/state1/DBIRTH/city1/area1/sp-area1-sensor1", message, 0)
  print "Publised to DBIRTH !"

  print "Message Published done!"

  mqttc.disconnect()

  #time.sleep(5)





