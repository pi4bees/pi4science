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


#logging_folder = glob.glob('/media/pi/EMTEC')[0]
dt = datetime.datetime.now()
file_folder = glob.glob('/media/pi/pi4science')[0]
#file_name = "pi4_{:%Y_%m_%d}.csv".format(dt)
file_name = file_folder + '/' + os.environ['USB_COLOR'] +  "_data.tsv"
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
	sensor4 = MCP9808.MCP9808(address = 0x1b)
        sensor5 = MCP9808.MCP9808(address = 0x1c)
        sensor6 = MCP9808.MCP9808(address = 0x1d)
        sensor7 = MCP9808.MCP9808(address = 0x1e)
        sensor8 = MCP9808.MCP9808(address = 0x1f)


	#print heading with date/time at begining of data collection "cycle"

	#print(datetime.ctime(datetime.now()))		

	# Initialize communication with the sensor.
	sensor.begin()
	sensor2.begin()
	sensor3.begin()
        sensor4.begin()
        sensor5.begin()
        sensor6.begin()
        sensor7.begin()
        sensor8.begin()

        
	# Optionally you can override the address and/or bus number:
	#sensor = MCP9808.MCP9808(address=0x20, busnum=2)
	
        
        #f = open(file_name, 'a+')
        #f.write('\n"{:%H:%M:%S}",'.format(dt))
        #f.write(str('MCP9808_temp      DHT22_hum%    KHT22_temp'))
        #f.close
                

	count = 0
    	while True:
        	s = DHT22.sensor(pi, 4)
                s.trigger()
                sleep(1)
                f = open(logging_file, 'a+')
                temp = sensor.readTempC()
                temp2 = sensor2.readTempC()
		temp3 = sensor3.readTempC()
                temp4 = sensor4.readTempC()
                temp5 = sensor5.readTempC()
                temp6 = sensor6.readTempC()
                temp7 = sensor7.readTempC()
                temp8 = sensor8.readTempC()

		
		dt = datetime.datetime.now()
                print('{0}	{1:0.4F}	{2:0.4F}	{3:0.4F}	{4:0.4F}        {5:0.4F}        {6:0.4F}        {7:0.4F}        {8:0.4F}	{9:0.2F}	{10:0.2F}'.format(dt.strftime("%d:%B:%Y:%H:%M:%S"), temp,	temp2, temp3, temp4, temp5, temp6, temp7, temp8, s.humidity()/1., s.temperature()/1.))
                f.write('{0}	{1:0.4F}	{2:0.4F}	{3:0.4F}        {4:0.4F}        {5:0.4F}        {6:0.4F}        {7:0.4F}        {8:0.4F}	{9:0.2F}	{10:0.2F}\n'.format(dt.strftime("%d:%B:%Y:%H:%M:%S"),temp,	temp2, temp3, temp4, temp5, temp6, temp7, temp8, s.humidity()/1., s.temperature()/1.))
	
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
		
		if(count == 120):
			call('git stash', shell = True)
			call('git pull', shell = True)
			call('git stash pop', shell = True)
			call('git commit -am "updating data"', shell = True)
			call('git push', shell = True)
			count = -1
		count += 1

if __name__=="__main__":
	main()
