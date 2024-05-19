# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# ADS1115
# This code is designed to work with the ADS1115_I2CADC I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Analog-Digital-Converters?sku=ADS1115_I2CADC#tabs-0-product_tabset-2

from smbus2 import SMBus
from datetime import datetime, timedelta

ADS1115_Addr = 0x48

def readA0():
	# Get I2C bus
	bus = SMBus(1)

	# ADS1115 address, 0x48(72)
	# Select configuration register, 0x01(01)
	#		0xC483(50307)	AINP = AIN0 and AINN = GND, +/- 2.048V
	#				Continuous conversion mode, 128SPS
	data = [0xC0,0x03]
	bus.write_i2c_block_data(0x48, 0x01, data)

	#	time = datetime.now()
	#	while (datetime.now() - time) < timedelta(seconds = 0.5):
	#		pass

	# ADS1115 address, 0x48(72)
	# Read data back from 0x00(00), 2 bytes
	# raw_adc MSB, raw_adc LSB
	# while True:
	data = bus.read_i2c_block_data(0x48, 0x00, 2)

	# Convert the data
	raw_adc = data[0] * 256 + data[1]

	if raw_adc > 32767:
		raw_adc -= 65535

	raw_adc  = (raw_adc * 6.144 / 32767)

	# # Output data to screen
	# print ("Digital Value of Analog Input on Channel-0: %.2f" %raw_adc)
	# time.sleep(1)

	return raw_adc

def readA1():
	# Get I2C bus
	bus = SMBus(1)

	# ADS1115 address, 0x48(72)
	# Select configuration register, 0x01(01)
	#		0xD483(54403)	AINP = AIN1 and AINN = GND, +/- 2.048V
	#				Continuous conversion mode, 128SPS
	data = [0xD0,0x03]
	bus.write_i2c_block_data(0x48, 0x01, data)

	#	time = datetime.now()
	#	while (datetime.now() - time) < timedelta(seconds = 0.5):
	#		pass

	# ADS1115 address, 0x48(72)
	# Read data back from 0x00(00), 2 bytes
	# raw_adc MSB, raw_adc LSB
	data = bus.read_i2c_block_data(0x48, 0x00, 2)

	# Convert the data
	raw_adc = data[0] * 256 + data[1]

	if raw_adc > 32767:
		raw_adc -= 65535

	raw_adc  = (raw_adc * 6.144 / 32767)

	# Output data to screen
	#print ("Digital Value of Analog Input on Channel-1: %d" %raw_adc)

	return raw_adc

def testModule():
	value0 = readA0()
	print ("Digital Value of Analog Input on Channel-0: %.2f" %value0)

	while (datetime.now() - time) < timedelta(seconds = 1):
		continue
	time = datetime.now()

	value1 = readA1()
	print ("Digital Value of Analog Input on Channel-1: %.2f" %value1)

	return


if __name__ == "__main__":
	time = datetime.now()
	while True:
		if (datetime.now() - time) > timedelta(seconds = 1):
			time = datetime.now()
			testModule()

# ADS1115 address, 0x48(72)
# Select configuration register, 0x01(01)
#		0xE483(58499)	AINP = AIN2 and AINN = GND, +/- 2.048V
#				Continuous conversion mode, 128SPS
#data = [0xE4,0x83]
#bus.write_i2c_block_data(0x48, 0x01, data)

#time.sleep(0.5)

# ADS1115 address, 0x48(72)
# Read data back from 0x00(00), 2 bytes
# raw_adc MSB, raw_adc LSB
#data = bus.read_i2c_block_data(0x48, 0x00, 2)

# Convert the data
#raw_adc = data[0] * 256 + data[1]

#if raw_adc > 32767:
#	raw_adc -= 65535

# Output data to screen
#print ("Digital Value of Analog Input on Channel-2: %d" %raw_adc)

# ADS1115 address, 0x48(72)
# Select configuration register, 0x01(01)
#		0xF483(62595)	AINP = AIN3 and AINN = GND, +/- 2.048V
#				Continuous conversion mode, 128SPS
#data = [0xF4,0x83]
#bus.write_i2c_block_data(0x48, 0x01, data)

#time.sleep(0.5)

# ADS1115 address, 0x48(72)
# Read data back from 0x00(00), 2 bytes
# raw_adc MSB, raw_adc LSB
#data = bus.read_i2c_block_data(0x48, 0x00, 2)

# Convert the data
#raw_adc = data[0] * 256 + data[1]

#if raw_adc > 32767:
#	raw_adc -= 65535

# Output data to screen
#print ("Digital Value of Analog Input on Channel-3: %d" %raw_adc)
