import network, time
from machine import Pin
import oled

def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True

if conectaWifi ("Jacobo", "1112160382"): #Estos son los datos de la red
    oled.mensaje("Conectado")
    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
else:
       print ("Imposible conectar")
       miRed.active (False)