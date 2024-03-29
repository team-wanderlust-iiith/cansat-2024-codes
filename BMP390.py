import time
import board
import adafruit_bmp3xx
#from smbus2 import SMBus

#i2c = SMBus(1)
i2c = board.I2C()
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)
bmp.filter_coefficient = 128
while True:
	print ("Pressure: {:6.1f}".format(bmp.pressure))
	print ("Temperature: {:5.2f}".format(bmp.temperature))
	print ("Altitude: {} meters".format(bmp.altitude))
	time.sleep(1)
