
the csv has two columns. First one is serial number and second one is the asset tag. 

The endpoint allows for user and blueprint also. They will need to be added to csv and parsing columns will nedd to be added. 
{
    "user": "1"
    "asset_tag": "testtrey",
    "blueprint_id": "be1a4d67-91d8-4d19-a927-c8be6e77b6b2"
}
Line 13 of script parses the columns and makes variables. srl is the serial number column and asst is the asset tag number. you could add usr srl asst bpid and the four columns would need to be Username, Serial number, Asset tag, blueprint id
Then script lines 46-48 would be changed to something like this 
--data-raw "{
\"user\": \"$usr\"
\"asset_tag\": \"$asst\"
\"blueprint_id\": \"$bpid\"
}"

you can have any 1 of the 3 parts to this above, you can do all 3, just 2 or 1. 
