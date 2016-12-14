#!/usr/bin/env bash

if [ -d "/media/pi/USB1" ]; then
	#sudo umount /media/pi/
	sudo umount /media/pi/USB1
fi

MOUNT_LOCATION=$(sudo blkid | grep /dev/s | cut -c1-9)
sudo mount $MOUNT_LOCATION /media/pi/ -o umask=000,uid=pi,gid=pi
sudo pigpiod
