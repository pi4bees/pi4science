#!/usr/bin/env bash

if [ -d "/media/pi/EMTEC" ]; then
	sudo umound /media/pi/EMTEC
fi

MOUNT_LOCATION=$(sudo blkid | grep /dev/s | cut -c1-9)
#sudo chown pi:pi -R pi
sudo mount $MOUNT_LOCATION /media/pi/ -o umask=000,uid=pi,gid=pi
