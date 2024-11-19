import utime
from microDNSSrv import MicroDNSSrv
from wifi_manager import WifiManager
import relaylib
from machine import Pin

relay1 = Pin(32, Pin.OUT)
relay2 = Pin(33, Pin.OUT)
relay3 = Pin(25, Pin.OUT)
relay4 = Pin(26, Pin.OUT)

# Fonction pour démarrer le serveur DNS
def start_dns_server():
    if MicroDNSSrv.Create({ '*' : '192.168.4.1' }):
        print("MicroDNSSrv démarré.")
        return True
    else:
        print("Erreur lors du démarrage de MicroDNSSrv...")
        return False

# Fonction pour arrêter le serveur DNS
def stop_dns_server():
    MicroDNSSrv.Stop()
    print("MicroDNSSrv arrêté.")

print("On rentre dans main.py")

# Boucle principale
dns_started = False


while True:
    wm.connect()  # Tente de se connecter à un réseau WiFi connu
    
    if wm.is_connected():
        if dns_started:
            print('Connecté au réseau WiFi:', wm.get_address())
            print('Arrêt du serveur DNS')
            stop_dns_server()
            dns_started = False
    else:
        print('Non connecté, en mode Point d\'Accès')
        print('Démarrage du serveur DNS')
        if not dns_started:
            dns_started = start_dns_server()
    
        # Test des relais
    print('Allumage du relais 1')
    relay1.on()
    utime.sleep(1)
    print('Extinction du relais 1')
    relay1.off()
    utime.sleep(1)
    print('Allumage du relais 2')
    relay2.on()
    utime.sleep(1)
    print('Extinction du relais 2')
    relay2.off()
    utime.sleep(1)
    print('Allumage du relais 3')
    relay3.on()
    utime.sleep(1)
    print('Extinction du relais 3')
    relay3.off()
    utime.sleep(1)
    print('Allumage du relais 4')
    relay4.on()
    utime.sleep(1)
    print('Extinction du relais 4')
    relay4.off()
    utime.sleep(1)
    
    utime.sleep(10)

