**Clone repo to local machine via this command in terminal**:
- git clone https://github.com/henro47/pi-kiosk-py

**Autostart script on startup (raspberry pi & Wayland/Wayfire window manager):**
 - nano ~./config/wayfire.ini
 - scroll to buttom of file in terminal
 - add:
    [autostart]
    1 = python3 $HOME/path_to_repo/main.py
 - CRTL + X to save file


**Autostart script on startup (raspberry pi & X11 window manager) Stable:**
 - sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
 - add to bottom of file:
   @lxterminal -e python3 /home/<username>/pi-kiosk-py/main.py &
 - CRTL + X to save file


**To switch between different window managers**:
   - sudo raspi-config
   - advanced configuration
