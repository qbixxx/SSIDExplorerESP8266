import network
from machine import Pin, I2C
from time import sleep
from ssd1306 import SSD1306_I2C

WIDTH = 128
HEIGHT = 64

i2c = I2C(scl = Pin(5), sda = Pin(4))

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

wifi = network.WLAN(network.STA_IF)

wifi.active(True)

oled.fill(0)
oled.text("Escaneando Redes",0,5)
oled.show()

lista_redes = wifi.scan()

oled.text("Listo!",0,30)
oled.show()
for red in lista_redes:
	print(red[0].decode()+" "+str(red[3]))

lista_redes_ordenada = list(sorted(lista_redes, reverse = True, key = lambda x: x[3]))

print("'''''''''''''''''''''''''")

for red in lista_redes_ordenada:
    print(red[0].decode()+" "+str(red[3]))

oled.fill(0)
oled.text(lista_redes_ordenada[0][0].decode(), 0, 0)
oled.text(str(lista_redes_ordenada[0][3]), 0, 10)

oled.text(lista_redes_ordenada[1][0].decode(), 0, 20)
oled.text(str(lista_redes_ordenada[1][3]), 0, 30)

oled.text(lista_redes_ordenada[2][0].decode(), 0, 40)
oled.text(str(lista_redes_ordenada[2][3]), 0, 50)
oled.show()
