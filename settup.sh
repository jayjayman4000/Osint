#!/bin/bash

echo "Updating system..."
sudo apt update

echo "Installing OSINT tools..."
sudo apt install -y theharvester recon-ng spiderfoot python3-pip

echo "Installing Sherlock..."
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
sudo pip3 install -r requirements.txt
cd ..

echo "Installing Python requirements..."
pip3 install -r requirements.txt

echo "Setup complete!"