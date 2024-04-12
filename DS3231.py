from smbus2 import SMBus
from time import sleep

DS3231_address = 0x68
CONV = 32


def convTemp(address):
	bus = SMBus(1)

	byte_control = bus.read_byte_data(address,0x0E)

	if byte_control&CONV == 0:
		bus.write_byte_data(address, 0x0E, byte_control|CONV)

	byte_control = bus.read_byte_data(address, 0x0E)

	while byte_control&CONV != 0:
		time.sleep(1)
		byte_control = bus.read_byte_data(address, 0x0E)

	return True


def readTemperature():
	bus = SMBus(1)

	convTemp(DS3231_address)
	byte_tmsb = bus.read_byte_data(DS3231_address,0x11)
	byte_tlsb = bus.read_byte_data(DS3231_address,0x12)

	tinteger = (byte_tmsb & 0x7f) + ((byte_tmsb & 0x80)>>7)* -2**8
	tdecimal = (byte_tmsb >> 7) * 2**(-1) + ((byte_tmsb & 0x40)>>6)*2**(-2)

	return tinteger + tdecimal


if __name__ == "__main__":
	while True:
		Celsius = readTemperature()
		print (Celsius, "*C")
		sleep(1)
