#!/usr/bin/python

import requests
from flash import run_cmd
import serial
from secrets import api_key

url = "https://api.uptimerobot.com/v2/getMonitors"
ser = serial.Serial ("/dev/ttyACM0", 9600, timeout = 1)

r = requests.post(url, data = {"api_key":api_key})
key_num = 0
if r.status_code == 200:
    status = r.json()
    
    for mon in status['monitors']:
        print("%30s : %d" % (mon['friendly_name'], mon['status']))
        if mon['status'] == 2:
            color = "0, 255, 0" 
        else:
            color = "255, 50, 50" 
        run_cmd(ser, "led.at %d %s" % (key_num, color))
        key_num += 1
