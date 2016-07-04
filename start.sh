#!/usr/bin/env bash

sudo umound /media/pi
MOUNT_LOCATION=$(sudo blkid | grep /dev/s | cut -c1-9)
sudo mount $MOUNT_LOCATION /media/pi/ -o umask=000,uid=pi,gid=pi
