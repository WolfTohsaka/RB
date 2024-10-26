from microDNSSrv import MicroDNSSrv
while True:
    if wm.is_connected():
        print('Connected!')
    else:
        print('Disconnected!')
        if MicroDNSSrv.Create({ '*' : '192.168.4.1' }) :
  print("MicroDNSSrv started.")
else :
  print("Error to starts MicroDNSSrv...")
    utime.sleep(10)
