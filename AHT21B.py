from smbus2 import SMBus
from time import sleep

AHT21B_Address = 0x38

## data = bus.read_byte(0x38)
## print (data)


def readTemperature():
	bus = SMBus(1)
	bus.write_i2c_block_data(0x38,0x70,[0xAC,0x33,0x00])
	data = bus.read_i2c_block_data(0x38,0x71,7)

	value = ((data[3] & 0x0F) << 16) | (data[4] << 8) | data[3]

	return ((200 * value) / 1048576) - 50


def testModule():
	"""Function to test AHT21B Temperature reading."""

##	while True:
##		print(f"{readTemp()} deg. C")
##		sleep(1)
	temperature = readTemperature()
	print(f"{temperature} deg. C")


if __name__ == "__main__":
	while True:
		testModule()
		sleep(1)
