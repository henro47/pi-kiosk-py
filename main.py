import subprocess
import sys

# Replace these with your Wi-Fi credentials
SSID = "WIFI_SSID"
PASSWORD = "WIFI_PASSWORD"
URL = "URL"

def connect_wifi(ssid, password, browser):
    try:
        # Create a new Wi-Fi connection
        subprocess.run(["nmcli", "device", "wifi", "connect", ssid, "password", password], check=True)
        print(f"Connected to {ssid}")
        if browser == "c":
            # Start Chrome in kiosk mode
            run_chrome(URL)
        elif browser == "f":
            # Start Firefox in kiosk mode
            run_firefox(URL)
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect: {e}")

def run_chrome(url):
    try:
        # Replace 'chromium-browser' with 'chromium' if that's your executable
        subprocess.run(["chromium-browser", "--noerrdialogs", "--disable-session-crashed-bubble", "--disable-infobars", "--start-fullscreen", "--kiosk", url], check=True)
        print("chrome started")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start Chromium: {e}")

def run_firefox(url):
    try:
        subprocess.run(["firefox", "-kiosk", url], check=True)
        print("firefox started")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start firefox: {e}")

if __name__ == "__main__":
    argumentList = sys.argv[1:]
    if len(argumentList) == 0:
        print("Please provide f (firefox) /c (chrome) as a command line argument")
        sys.exit(1)
    if str(argumentList[0]) != "f" and str(argumentList[0]) != "c":
        print("Invalid argument. Please provide f (firefox) /c (chrome) as a command line argument")
        sys.exit(1)
    connect_wifi(SSID, PASSWORD, argumentList[0])
