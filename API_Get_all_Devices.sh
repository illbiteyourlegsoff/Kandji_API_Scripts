#!/bin/sh -x

###########################################################
#
# Simple script to get all devices
#
#############################################################


###kandji sub and domain ie if url is https://server.kandji.io knjsub = server 
knjsub="server"


###This is variable for bearer token, presently it is $1  so it will be script then Tokens
apiToken="addtokenhere"
#token="$1" ### you can comment out top variable and uncomment this one if you will run script with token after ie.. (./script.sh tokenhere)

##################################################Variables end ###############################################################



###command to delete Toeken
curl --location --request GET "https://"${knjsub}".clients.us-1.kandji.io/api/v1/devices/" \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $apiToken"

