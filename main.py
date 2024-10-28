import subprocess

# Replace these with your Wi-Fi credentials
SSID = "SSID"
PASSWORD = "PASSWORD"
URL = "URL"

def connect_wifi(ssid, password):
    try:
        # Create a new Wi-Fi connection
        subprocess.run(["nmcli", "device", "wifi", "connect", ssid, "password", password], check=True)
        print(f"Connected to {ssid}")
        run_chrome(URL)
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect: {e}")

def run_chrome(url):
    try:
        # Replace 'chromium' with 'chromium-browser' if that's your executable
        subprocess.run(["chromium-browser --kiosk ", url], check=True)
        print("chrome started")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start Chromium: {e}")

if __name__ == "__main__":
    connect_wifi(SSID, PASSWORD)