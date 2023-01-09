#!/usr/bin/python3
from typing import Dict

#####Server instance name
# instnme="trey"  ### if trey.kandji.io was your instance, you would just put trey
instnme = "treyhowell"

####Enterprise API token
# token="add token here"
token = '60283808-8361-4446-bebc-60c6e2c2cb76'

####location of csv file. Will make cleaner later
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

csv_file = filedialog.askopenfilename()
#csv_file = '/Users/treyhowell/Desktop/assettags.csv'

####required modules
import csv
import requests

#########################Functions

####function to get Serial
def get_serial(srl):
    url = "https://" + instnme + ".clients.us-1.kandji.io/api/v1/devices/?serial_number=" + srl

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    global devid
    devid = response.text[15:51]


####Function to set asset tag
global devid
def set_asset(assttg):
    url2 = "https://" + instnme + ".clients.us-1.kandji.io/api/v1/devices/" + devid

    payload2 = {
        'asset_tag': '' + assttg
    }

    headers2 = {
        'Authorization': 'Bearer ' + token
    }

    response2 = requests.request("PATCH", url2, headers=headers2, data=payload2)

####parsing csv and running functions
with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for stuff in csvreader:
        get_serial(stuff[0])
        set_asset(stuff[1])







