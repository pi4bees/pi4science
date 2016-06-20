#!/usr/bin/env python
import pigpio

def main():
	from time import sleep
	pi = pigpio.pi()
	import DHT22
	for i in range(10):
		s = DHT22.sensor(pi, 4)
		s.trigger()
		sleep(.01)
		print('{:3.2f}	{:3.2f}'.format(s.humidity()/1., s.temperature()/1.))
		sleep(10)
		s.cancel()
	pi.stop

if __name__=="__main__":
	main()
