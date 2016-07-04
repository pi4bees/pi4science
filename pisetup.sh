#!/usr/bin/env bash

echo "UUID=30A3-8EE8 /media/pi vfat user,umask=000,utf8,flush,noauto 0 0" >> /et/fstab
sudo mount -a

PI_VERSION=$(cat /proc/cpuinfo | grep Revision | cut -c12-18)
if [ $PI_VERSION == "a22082" ]; then
	read -p "add id_rsa"
	mv ~/Downloads/id_rsa ~/.ssh
	mv ~/Downloads/id_rsa.pub ~/.ssh
	chmod 600 ~/.ssh/id_rsa
	chmod 600 ~/.ssh/id_rsa.pub
	eval "$(ssh-agent -s)"
	ssh-add ~/.ssh/id_rsa
	ssh -T git@github.com
	cd /media/pi
	git clone git@github.com:pi4bees/pi4science.git
	cd pi4science
	git checkout gh-pages
	git config --global user.email "hns36@cornell.edu"
	git config --global user.name "pi4bees"
fi

