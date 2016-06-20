#!/usr/bin/env python
import pigpio
from time import sleep
from PIGPIO import DHT22
import Adafruit_MCP9808.MCP9808 as MCP9808
from datetime import datetime


	#importing commands/dir needed for USB pushing
import os, glob, time, datetime


logging_folder = glob.glob('/media/usb0/')[0]
dt = datetime.datetime.now()
file_name = "temp_log_{:%Y_%m_%d}.csv".format(dt)
logging_file = logging_folder + '/' + file_name



# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

def main():
        pi = pigpio.pi()

	# Default constructor will use the default I2C address (0x18) and pick a default I2C bus.
	#
	# For the Raspberry Pi this means you should hook up to the only exposed I2C bus
	# from the main GPIO header and the library will figure out the bus number based
	# on the Pi's revision.
        sensor = MCP9808.MCP9808()

	#print heading with date/time at begining of data collection "cycle"

	#print(datetime.ctime(datetime.now()))

	# Initialize communication with the sensor.
        sensor.begin()

	# Optionally you can override the address and/or bus number:
	#sensor = MCP9808.MCP9808(address=0x20, busnum=2)

        f = open(logging_file, 'a+')
        f.write('\n"{:%H:%M:%S}",'.format(dt))
        f.write(str('MCP9808_temp      DHT22_hum%    KHT22_temp'))

        print('MCP9808_temp	DHT22_hum	DHT22_temp')
        while True:
                s = DHT22.sensor(pi, 4)
                s.trigger()
                sleep(1)
                temp = sensor.readTempC()
                print('{0:0.4F}	{1:0.2F}	{2:0.2F}'.format(temp, s.humidity()/1., s.temperature()/1.))

                f = open(logging_file, 'a+')
                f.write('\n"{:%H:%M:%S}",'.format(dt))
                f.write(str(temp))
                f.close

                sleep(30)
                s.cancel()
                pi.stop

if __name__=="__main__":
	main()
