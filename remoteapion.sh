#!/bin/bash -x
######This script will activate remote desktop using API
####create a API token just for Remote Desktop and Device list and add the token below leaving in quotes
#####once token and instance name is added just add to Custom Script and add what blueprints you want it for. 
# this can be used to turn off remote also changing true to false. 


##########################################Variables

#####Server instance name
instnme="trey"  ### if trey.kandji.io was your instance, you would just put trey



####Enterprise API token
token="add token here"


#####################################################end of variables




####this will send the call to enable remote desktop. Change to false below if you want to disable remote desktop
curl --location --request POST 'https://'$instnme'.clients.us-1.kandji.io/api/v1/devices/'$DEVICE_ID'/action/remotedesktop/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer '$token'' \
--data-raw '{
    "EnableRemoteDesktop": true
}'


