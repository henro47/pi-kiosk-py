Clone repo to local machine via this command in terminal:
- git clone https://github.com/henro47/pi-kiosk-py

Autostart script on startup (raspberry pi):
 - sudo nano ~./config/wayfire.ini
 - scroll to buttom of file in terminal
 - add:
    [autostart]
    1 = python3 $HOME/path_to_repo/main.py