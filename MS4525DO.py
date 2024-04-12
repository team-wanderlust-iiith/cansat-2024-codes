from smbus2 import SMBus
from time import sleep

MS4525D0_Address = 0x28

#bus = SMBus(1)

def readAirSpeed():
	bus = SMBus(1)
	data = bus.read_byte(MS4525D0_Address)

	return data


def testModule():
	print ("Air Speed = ", readAirSpeed())


if __name__ == "__main__":
	while True:
		testModule()
		sleep(1)
