#!/bin/bash -x


##########################################Variables

#####Server instance name
#instnme="trey"  ### if trey.kandji.io was your instance, you would just put trey
instnme="trey"


####Enterprise API token
#token="add token here"
token="xxxxxxx-xxxxx-xxxx-xxxx-xxxxxxxxxx"

###path to csv file. This can be commented out and the line for input below can be used once I get around the new security and osascript. It is double quoted to make the loop work. keep double quoted.
INPUT=""/Users/trey/Desktop/assettags.csv""

#####################################################end of variables


################ This is commented out for now till I get this working
#INPUT="$(osascript -e 'Tell application "System Events" to  return POSIX path of (choose file with prompt "Select an CSV file")')"

#Adds a line or the last one will not be picked up in script
echo " " >> "$INPUT"


##parseing through CSV file and starting the loop of the csv file
SaveIFS=$IFS
IFS=","
while read srl asst
do


####get this device from the device list and pull out Device UUID
rawCall=$(curl --location --request GET 'https://'$instnme'.clients.us-1.kandji.io/api/v1/devices/?serial_number='$srl'' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer '$token'' | cut -b 16-51)



####This adds the asset tag to each device. This endpoint can add IDP and Blueprint info also. It is not in this script. 
curl --location --request PATCH 'https://'$instnme'.clients.us-1.kandji.io/api/v1/devices/'$rawCall'/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer '$token'' \
--data-raw "{
\"asset_tag\": \"$asst\"
}"

###end of the loop
done < $INPUT
IFS=$SaveIFS