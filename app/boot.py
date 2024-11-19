import webrepl
import senko

# Import the library:
from wifi_manager import WifiManager

# Initialize it
wm = WifiManager()

# By default the SSID is WiFiManager and the password is wifimanager.
# You can customize the SSID and password of the AP for your needs:
wm = WifiManager(ssid="RaidBox",password="RaidBox1")
webrepl.start()

# Start the connection:
wm.connect()


OTA = senko.Senko(
  user="WolfTohsaka", # Required
  repo="RB", # Required
  branch="master", # Optional: Defaults to "master"
  working_dir="app", # Optional: Defaults to "app"
  files = ["boot.py", "main.py"]
)


if OTA.update():
    print("Updated to the latest version! Rebooting...")
    machine.reset()