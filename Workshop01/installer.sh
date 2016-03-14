#! /bin/sh
#
# installer.sh
# Copyright (C) 2016 cameron <www.candidcypher.com>
#
# Distributed under terms of the MIT license.
#


echo "This is a basic installer script for installing the software used in the 
Austin IoT Workshops. This script will automate the process of installing the 
required software on your Raspberry Pi."

sudo apt-get update && sudo apt-get upgrade

cd ~/
mkdir ~/Downloads
cd ~/Downloads
wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh

bash Mini*

sudo apt-get install git mosquitto
