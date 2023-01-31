from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import framebuf # Módulo para visualizar imagenes en pbm

#Tamaño de la pantalla
ancho = 128
alto = 64

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(ancho, alto, i2c)
print(i2c.scan())

def mensaje(x):
    oled.text(x, 20, 25, 1)
    oled.show()
    time.sleep(2)
    oled.fill(0)
    
def mostrarLogo(ruta):
    dibujo = open(ruta, "rb")  # Abrir en modo lectura de bits
    dibujo.readline() # metodo para ubicarse en la primera linea de los bits
    xy = dibujo.readline() # ubicarnos en la segunda línea
    x = int(xy.split()[0])  # split devuelve una lista de los elementos de la variable solo 2 elementos
    y = int(xy.split()[1])
    icono = bytearray(dibujo.read())  # guardar en matriz de bites
    dibujo.close()
    return framebuf.FrameBuffer(icono, x, y, framebuf.MONO_HLSB)  #Utilizamos el metodo MONO_HLSB
print(i2c.scan())

oled.blit(mostrarLogo("Imagen/AcuaCon_pq.pbm"), 0, 0) #Ruta y sitio de ubicación de la imagen
oled.show()  #mostrar en la oled
time.sleep(3) # Espera de 3 segundos
oled.fill(0)
oled.show()

oled.text('AcuaCon', 40, 30)
oled.show()
time.sleep(3)
oled.fill(0)
oled.show()