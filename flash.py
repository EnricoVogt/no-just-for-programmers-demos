#!/usr/bin/python
import serial
import time

flash_time = 0.3
num_flashes = 5
flash_color = "255 50 50" 

def run_cmd(ser, cmd):
    ser.write (cmd)
    ser.write ("\n")
    while True:
        resultLine = ser.readline ()
        resultLine = resultLine.rstrip ()
        if resultLine == ".":
            break

if __name__ == '__main__':

    ser = serial.Serial ("/dev/ttyACM0", 9600, timeout = 1)
    for i in range(num_flashes):
        run_cmd(ser, "led.setAll %s" % flash_color)
        time.sleep(flash_time)
        run_cmd(ser, "led.setAll 0 0 0")
        time.sleep(flash_time)
