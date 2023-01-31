import _thread
from machine import enable_irq, disable_irq, Timer
from utime import sleep, ticks_ms, ticks_diff
import oled
import wifi
import Caudalimetro

#Imprimir logo
oled.mostrarLogo()

#Conectar Wifi
wifi.conectaWifi()
def red():
    if wifi.conectaWifi (wifi.ssid, wifi.passwd):
        oled.mensaje("Conectado")
        print ("Conexión exitosa!")
        print('Datos de la red (IP/netmask/gw/DNS):', wifi.miRed.ifconfig())
    else:
        print ("Imposible conectar")
        oled.mensaje("Sin conexion","a red")
        miRed.active (False)