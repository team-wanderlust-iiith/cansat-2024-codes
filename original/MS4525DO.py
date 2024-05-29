from smbus2 import SMBus
from time import sleep
import math

MS4525D0_Address = 0x28

#bus = SMBus(1)

def readRaw():
	bus = SMBus(1)
	data = bus.read_i2c_block_data(MS4525D0_Address,0x00,4)
	return data


def testModule():
	data = readRaw()
	Press_H = data[0]
	Press_L = data[1]
	Temp_H = data[2]
	Temp_L = data[3]
	status = (Press_H >>6) & 0x03
	Press_H = Press_H & 0x3F
	Pressure = (Press_H << 8) | Press_L
	Pressure_R = ((Pressure - 819.15)/14744.7)
	Pressure_R = Pressure_R  - 0.49060678
	Pressure_R = abs(Pressure_R)
	Pressure = Pressure * 0.0009155
	V = (Pressure_R * 13789.5144/1.225)
	Velocity = math.sqrt(V)

	Temp_L = Temp_L >> 5
	Temperature = (Temp_H << 3) | Temp_L
	Temperature = Temperature*0.09770395701 -50

#	print (Pressure)
	print ("Air Speed:", Velocity)
#	print (Temperature)
	#print ("Air Speed = ", airSpeed)

if __name__ == "__main__":
	while True:
		testModule()
		sleep(1)
