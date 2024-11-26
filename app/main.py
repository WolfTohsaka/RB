import utime
from microDNSSrv import MicroDNSSrv
from wifi_manager import WifiManager
import relaylib
from machine import ADC, Pin
import webrepl
import templib
import sys
from micropython import const
import asyncio
import aioble
import bluetooth
import random
import struct

print("On rentre dans main.py")

# ruff: noqa: E402
sys.path.append("")

print("on prépare le bluetooth")
# org.bluetooth.service.environmental_sensing
_ENV_SENSE_UUID = bluetooth.UUID(0x181A)
# org.bluetooth.characteristic.temperature
_ENV_SENSE_TEMP_UUID = bluetooth.UUID(0x2A6E)
# org.bluetooth.characteristic.gap.appearance.xml
_ADV_APPEARANCE_GENERIC_THERMOMETER = const(768)

print("on set le timer pour le bacon")
# How frequently to send advertising beacons.
_ADV_INTERVAL_MS = 250_000

print("on démarre le serveur GATT")
# Register GATT server.
temp_service = aioble.Service(_ENV_SENSE_UUID)
temp_characteristic = aioble.Characteristic(
    temp_service, _ENV_SENSE_TEMP_UUID, read=True, notify=True
)
aioble.register_services(temp_service)

print("on définit le helper")
# Helper to encode the temperature characteristic encoding (sint16, hundredths of a degree).
def _encode_temperature(temp_deg_c):
    return struct.pack("<h", int(temp_deg_c * 100))

print("on définit sensor_task()")
async def sensor_task():
    t = 24.5
    while True:
        temp_characteristic.write(_encode_temperature(t), send_update=True)
        t += random.uniform(-0.5, 0.5)
        print(t)
        print(_encode_temperature(t).hex())
        print(Temp)
        await asyncio.sleep_ms(1000)

print("on définit peripheral_task()")
# Serially wait for connections. Don't advertise while a central is
# connected.
async def peripheral_task():
    while True:
        async with await aioble.advertise(
            _ADV_INTERVAL_MS,
            name="RelayBox",
            services=[_ENV_SENSE_UUID],
            appearance=_ADV_APPEARANCE_GENERIC_THERMOMETER,
        ) as connection:
            print("Connection from", connection.device)
            await connection.disconnected(timeout_ms=None)
print("on run les 2 en concurrence")
# Run both tasks.
async def main():
    t1 = asyncio.create_task(sensor_task())
    t2 = asyncio.create_task(peripheral_task())
    await asyncio.gather(t1, t2)

asyncio.run(main())
print("je pense qu'on ne rentrera jamais ici.")
# Configuration de l'ADC
adc = ADC(Pin(34))  # Utiliser GPIO34
adccompensation = ADC(Pin(36))
adc.width(ADC.WIDTH_12BIT)  # Résolution 12 bits
adccompensation.width(ADC.WIDTH_12BIT)  # Résolution 12 bits


R_reference = 988  # Résistance de référence (988 Ω)

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
    print("MicroDNSSrv arrêté. WebREPL démarré")



# Boucle principale
dns_started = False


while True:
    wm.connect()  # Tente de se connecter à un réseau WiFi connu
    
    if wm.is_connected():
        if OTA.fetch():
            print("Nouvelle version disponible ! Redémarrer la carte.")
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
    
    
    adc_value = adc.read()
    adccompensation_value = adccompensation.read()

    voltage = (adc_value - adccompensation / 4095) * 3.3  # Conversion en volts
    
    # Calculer la résistance inconnue (R) avec la loi d'Ohm
    if voltage > 0:  # Éviter la division par zéro
        R_unknown = R_reference * (3.3 / voltage)
    else:
        R_unknown = float('inf')  # Si la tension est nulle, R est infinie

    print(R_unknown)

    utime.sleep(10)

