from machine import Pin, Timer, PWM
import network, time, utime, urequests
import oled

sensorFlujo = Pin(35, Pin.IN) #Declaramos el pin del sensor
numPulsos = 0 # Variable número de pulsos
reloj = Timer(0) #Para que me ayude a determinar la frecuencia
led = Pin(2, Pin.OUT) #Declaramos el pin del led
servo = PWM(Pin(32), freq=50) #Declaramos el pin del servomotor
inicio = time.ticks_ms() #Variable de manejo del tiempo

#Conexión a thingspeak
url = "https://api.thingspeak.com/update?api_key=N3NVO82C61DX9ZP5&field1=0"

while True:
    def conteo(pin): #Función para conteo de pulsos
        global numPulsos #Variable global
        numPulsos += 1

    def freq(timer): #Función de temporizado
        global numPulsos, F
        frec = numPulsos     
        F = frec / 7.5    
        print (f"Caudal= {F}")
        numPulsos = 0  

    sensorFlujo.irq(trigger = Pin.IRQ_RISING, handler = conteo)
    reloj.init(mode= Timer.PERIODIC, period= 1000, callback= freq)

#Visualización resultados en thingspeak
    respuesta = urequests.get(url+"&field1="+str(numPulsos)) 
    print(respuesta.status_code) #Código de respuesta de estado - si es 200 indica solicitud exitosa
    respuesta.close ()

#Primera acción: encendido de led y mensaje de precaución en pantalla
    if time.ticks_diff(time.ticks_ms(), inicio) > 2000:#Control del tiempo de encendido del led
        led.value(1) #Prende el led
        oled.mensaje("Precaucion") #Imprime mensaje en la pantalla
        utime.sleep(2) #Encendido por 2 segundos
        led.value(0) #Apaga

#Segunda acción: encendido de servomotor para cerrado del grifo y mensaje de flujo cerrado en pantalla
    if time.ticks_diff(time.ticks_ms(), inicio) > 4000:#Control del tiempo de encendido del servo
#Trabajando en microsegundos
#500000 para posición 0°
#2500000 para posición 180°
#4000 para el manejo de la velocidad (variable pulso)
        for pulso in range (500000, 2500000, 4000):
            servo.duty_ns(pulso)
            time.sleep_ms(1)

#Para que el servo regrese al punto inicial de 180° a 0°
        for pulso in range (2500000, 500000, -4000):
            servo.duty_ns(pulso)
            time.sleep_ms(1)
        oled.mensaje("Flujo cerrado") #Mensaje en pantalla
        break #Detengo la ejecución del ciclo.
    