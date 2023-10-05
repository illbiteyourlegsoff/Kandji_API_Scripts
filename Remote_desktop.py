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





################Api Call to set remote

url2 = "https://" + instnme + ".clients.us-1.kandji.io/api/v1/devices/" + '$DEVICE_ID' + "/action/remotedesktop/"

payload2 = json.dumps({
  "EnableRemoteDesktop": False
})

headers2 = {
     'Content-Type': 'application/json',
     'Authorization': 'Bearer ' + token
 }

response = requests.request("POST", url2, headers=headers2, data=payload2)
###############end of API call to set remote