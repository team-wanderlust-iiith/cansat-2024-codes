from time import sleep
import board
import adafruit_bmp3xx
#from smbus2 import SMBus

#i2c = SMBus(1)

def setup():
	i2c = board.I2C()
	sensor = adafruit_bmp3xx.BMP3XX_I2C(i2c)
	sensor.filter_coefficient = 128

	return sensor


def readPressure():
	bmp = setup()
	return bmp.pressure


def readTemperature():
	bmp = setup()
	return bmp.temperature


def readAltitude():
	bmp = setup()
	return bmp.altitude


def testModule():
	print ("Pressure: {:6.1f}".format(readPressure()))
	print ("Temperature: {:5.2f}".format(readTemperature()))
	print ("Altitude: {} meters".format(readAltitude()))


if __name__ == "__main__":
	while True:
		testModule()
		sleep(1)
