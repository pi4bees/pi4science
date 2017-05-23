#!/usr/bin/env python
from subprocess import call
import imp
pigpio = imp.load_source("pigpio", '/usr/local/lib/python2.7/dist-packages/pigpio.py')
from time import sleep
from PIGPIO import DHT22
import Adafruit_MCP9808.MCP9808 as MCP9808
from datetime import datetime
import os, glob, time, datetime

dt = datetime.datetime.now()
file_folder = glob.glob('/media/pi/pi4science')[0]
file_name = file_folder + '/purple_triangle_data.tsv'
logging_file = file_name

# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0

pi = pigpio.pi()

# Default constructor will use the default I2C address (0x18) and pick a default I2C bus.
#
# For the Raspberry Pi this means you should hook up to the only exposed I2C bus
# from the main GPIO header and the library will figure out the bus number based
# on the Pi's revision.
sensor = MCP9808.MCP9808(address = 0x18)
sensor2 = MCP9808.MCP9808(address = 0x19)
sensor3 = MCP9808.MCP9808(address = 0x1a)
sensor4 = MCP9808.MCP9808(address = 0x1b)
sensor5 = MCP9808.MCP9808(address = 0x1c)

one = True
two = True
three = True
four = True
five = True
try:
    sensor.begin()
except:
    one = False
    pass
try:
    sensor2.begin()
except:
    two = False
    pass
try:
    sensor3.begin()
except:
    three = False
    pass
try:
    sensor4.begin()
except:
    four = False
    pass
try:
    sensor5.begin()
except:
    five = False
    pass


# Optionally you can override the address and/or bus number:
#sensor = MCP9808.MCP9808(address=0x20, busnum=2)


while True:
    s = DHT22.sensor(pi, 4)
    s.trigger()
    sleep(1)
    f = open(logging_file, 'a+')
    temp = -999
    temp2 = -999
    temp3 = -999
    temp4 = -999
    temp5 = -999
    if one:
        try:
            temp = sensor.readTempC()
        except:
            pass
    else:
        try:
            sensor.begin()
            one = True
        except:
            one = False
            pass
    if two:
        try:
            temp2 = sensor2.readTempC()
        except:
            pass
    else:
        try:
            sensor2.begin()
            two = True
        except:
            two = False
            pass
    if three:
        try:
            temp3 = sensor3.readTempC()
        except:
            pass
    else:
        try:
            sensor3.begin()
            three = True
        except:
            three = False
            pass
    if four:
        try:
            temp4 = sensor4.readTempC()
        except:
            pass
    else:
        try:
            sensor4.begin()
            four = True
        except:
            four = False
            pass
    if five:
        try:
            temp5 = sensor5.readTempC()
        except:
            pass
    else:
        try:
            sensor5.begin()
            five = True
        except:
            five = False
            pass


    dt = datetime.datetime.now()
    print('{0}	{1:0.4F}	{2:0.4F}	{3:0.4F}	{4:0.4F}    {5:0.4F}	{6:0.2F}	{7:0.2F}'.format(dt.strftime("%d:%B:%Y:%H:%M:%S"), temp,	temp2, temp3, temp4, temp5, s.humidity()/1., s.temperature()/1.))
    f.write('{0}\t{1:0.4F}\t{2:0.4F}\t{3:0.4F}\t{4:0.4F}\t{5:0.4F}\t{6:0.2F}\t{7:0.2F}\n'.format(dt.strftime("%d:%B:%Y:%H:%M:%S"),temp, temp2, temp3, temp4, temp5, s.humidity()/1., s.temperature()/1.))

    sleep(10)
    s.cancel()
    pi.stop
    f.close

    #if(count == 120):
    #    call('git stash', shell = True)
    #    call('git pull', shell = True)
    #    call('git stash pop', shell = True)
    #    call('git commit -am "updating data"', shell = True)
    #    call('git push', shell = True)
    #    count = -1
    #count += 1

