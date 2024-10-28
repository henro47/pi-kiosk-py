#!/bin/bash
# started from the /etc/xdg/LXDE-pi/autostart file (reminder)

cd /home/inspire/Documents/pi-kiosk-py
sleep 10
echo "Stating pi script..."
lxterminal --working-directory='/home/inspire/pi-kiosk-py' --command='python3 main.py'