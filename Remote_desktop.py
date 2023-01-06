#!/usr/bin/python3

#####################
#
# sets remote destop to on, can be used to turn off also
#requires Python3 and xcode. Modeule requests needed also
#
##############################
###################Variables
#####Server instance name
# instnme="trey"  ### if trey.kandji.io was your instance, you would just put trey
instnme = "trey"

####Enterprise API token
# token="add token here"
token = '8382fbf2-9fa1xxxxxxxxx4ee9e8ae3'


#################end of variables

#######install required modules
import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m','pip', 'install', 'requests'])

#######end of module installs





#######################Serial number
import json
import subprocess
system_profile_data = subprocess.Popen(
    ['system_profiler', '-json', 'SPHardwareDataType'], stdout=subprocess.PIPE)
data = json.loads(system_profile_data.stdout.read())
serial = data.get('SPHardwareDataType', {})[0].get('serial_number')
###serial = "C02GLrrr7"  ####option to hardcode
######end of serial number

####the Api Call to get uuid/device id
import requests
url = "https://" + instnme + ".clients.us-1.kandji.io/api/v1/devices/?serial_number=" + serial

payload={}
headers = {
     'Authorization': 'Bearer ' + token
 }

response = requests.request("GET", url, headers=headers, data=payload)



####make variable of just the uuid
devid = response.text[15:51]
#########end of api call to get UUID/device id


################Api Call to set remote

url2 = "https://" + instnme + ".clients.us-1.kandji.io/api/v1/devices/" + devid + "/action/remotedesktop/"

payload2 = json.dumps({
  "EnableRemoteDesktop": False
})

headers2 = {
     'Content-Type': 'application/json',
     'Authorization': 'Bearer ' + token
 }

response = requests.request("POST", url2, headers=headers2, data=payload2)
###############end of API call to set remote