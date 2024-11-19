# Import the library:
from wifi_manager import WifiManager

# Initialize it
wm = WifiManager()

# By default the SSID is WiFiManager and the password is wifimanager.
# You can customize the SSID and password of the AP for your needs:
wm = WifiManager(ssid="RaidBox",password="RaidBox1")

# Start the connection:
wm.connect()