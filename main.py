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
oled.text("Scanning...",0,5)
oled.show()

ssid_list = wifi.scan()

oled.text("Done!",0,30)
oled.show()
for ssid in ssid_list:
	print(ssid[0].decode()+" "+str(ssid[3]))

sorted_ssid = list(sorted(ssid_list, reverse = True, key = lambda x: x[3]))


for ssid in sorted_ssid:
    print(ssid[0].decode()+" "+str(ssid[3]))

oled.fill(0)
oled.text(sorted_ssid[0][0].decode(), 0, 0)
oled.text(str(sorted_ssid[0][3]), 0, 10)

oled.text(sorted_ssid[1][0].decode(), 0, 20)
oled.text(str(sorted_ssid[1][3]), 0, 30)

oled.text(sorted_ssid[2][0].decode(), 0, 40)
oled.text(str(sorted_ssid[2][3]), 0, 50)
oled.show()
