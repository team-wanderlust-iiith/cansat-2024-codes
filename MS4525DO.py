from smbus2 import SMBus
from time import sleep
import math

MS4525D0_Address = 0x28

#bus = SMBus(1)

def readPressure():
	bus = SMBus(1)
	data = bus.read_byte(MS4525D0_Address)
	return data


def readAirSpeed():
	pressure = readPressure()
	airSpeed = math.sqrt(pressure / (2 * 1.225))
	return airSpeed

def testModule():
	print ("Air Speed = ", readAirSpeed())
	#print ("Air Speed = ", airSpeed)

if __name__ == "__main__":
	while True:
		testModule()
		sleep(1)
