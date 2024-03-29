from smbus2 import SMBus
from time import sleep

bus = SMBus(1)
AHT21B_Address = 0x38

data = bus.read_byte(0x38)
print (data)

def  read_temp():
	value = readSensor(False)
	return ((200*value)/1048576)-50

bus.write_i2c_block_data(0x38,0x70,[0xAC,0x33,0x00])
data = bus.read_i2c_block_data(0x38,0x71,7)
#bus.write_i2c_block_data(0x38,0x38,[0xAC,0x33,0x00])
#data = bus.read_i2c_block_data(0x38,0x38,7)
print (data)
