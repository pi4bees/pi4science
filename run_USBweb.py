#!/usr/bin/env python
from subprocess import call
import imp
pigpio = imp.load_source("pigpio", '/usr/local/lib/python2.7/dist-packages/pigpio.py')
from time import sleep
from PIGPIO import DHT22
import Adafruit_MCP9808.MCP9808 as MCP9808
from datetime import datetime


	#importing commands/dir needed for USB pushing
import os, glob, time, datetime


#logging_folder = glob.glob('/media/usb0/pi4science')[0]
dt = datetime.datetime.now()
#file_name = "pi4_{:%Y_%m_%d}.csv".format(dt)
file_name = os.environ['USB_COLOR'] +  "_data.tsv"
#logging_file = logging_folder + '/' + file_name
logging_file = file_name



# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

def main():

	global dt
        pi = pigpio.pi()

	# Default constructor will use the default I2C address (0x18) and pick a default I2C bus.
	#
	# For the Raspberry Pi this means you should hook up to the only exposed I2C bus
	# from the main GPIO header and the library will figure out the bus number based
	# on the Pi's revision.
	sensor = MCP9808.MCP9808(address = 0x18)
	sensor2 = MCP9808.MCP9808(address = 0x19)
	sensor3 = MCP9808.MCP9808(address = 0x1a)
	

	#print heading with date/time at begining of data collection "cycle"

	#print(datetime.ctime(datetime.now()))		

	# Initialize communication with the sensor.
	sensor.begin()
	sensor2.begin()
	sensor3.begin()

	# Optionally you can override the address and/or bus number:
	#sensor = MCP9808.MCP9808(address=0x20, busnum=2)
	
        
        #f = open(logging_file, 'a+')
        #f.write('\n"{:%H:%M:%S}",'.format(dt))
        #f.write(str('MCP9808_temp      DHT22_hum%    KHT22_temp'))
        #f.close
                

    	while True:
        	s = DHT22.sensor(pi, 4)
                s.trigger()
                sleep(1)
                f = open(logging_file, 'a+')
                temp = sensor.readTempC()
                temp2 = sensor2.readTempC()
		temp3 = sensor3.readTempC()
		dt = datetime.datetime.now()
                print('{0:0.4F}	{1:0.4F}	{2:0.4F}	{3:0.2F}	{4:0.2F}'.format(temp,	temp2, temp3,  s.humidity()/1., s.temperature()/1.))
                f.write('{0:0.4F}	{1:0.4F}	{2:0.4F}	{3:0.2F}	{4:0.2F}'.format(temp,	temp2, temp3,  s.humidity()/1., s.temperature()/1.))
	
		#writing in line for temp1 data
		#f.write('\n"{:%d:%B:%Y:%H:%M:%S}",'.format(dt)) 
                #f.write('MCP9808_temp,{0:0.4F},'.format(temp,))
             
		#writing line for temp2 data 
		#f.write('\n"{:%d:%B:%Y:%H:%M:%S}",'.format(dt)) 
                #f.write('MCP9808_temp2,{0:0.4F},'.format(temp2,))

		# writing line for temp3 data
		#f.write('\n"{:%d:%B:%Y:%H:%M:%S}",'.format(dt)) 
            	#f.write('MCP9808_temp3,{0:0.4F},'.format(temp3,))
                

		#writing line for DHT22 temp and humidity
		#f.write('\n"{:%d:%B:%Y:%H:%M:%S}",'.format(dt)) 
                #f.write('DHT22_temp,{0:0.2F},'.format(s.temperature()/1.))


		#f.write('\n"{:%d:%B:%Y:%H:%M:%S}",'.format(dt)) 
                #f.write('DHT22_hum,{0:0.2F},'.format(s.humidity()/1.))



		#f.write('{0:0.4F},{1:0.4F},{2:0.2F},{3:0.2F}'.format(temp,	temp2,   s.humidity()/1., s.temperature()/1.))
		sleep(30)
                s.cancel()
                pi.stop
                f.close
		call('git commit -am "updating data"', shell = True)
		call('git push', shell = True)

if __name__=="__main__":
	main()
