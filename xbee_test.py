from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee64BitAddress
from datetime import datetime, timedelta

PANID = b"\x20\x85"
CANSAT_ADDR = "0013A2004108F519"
GND_ADDR = "0013A200410908BE"
CANSAT_PORT = "/dev/serial0"
CANSAT_BAUD_RATE = 9600

REMOTE64ADDR = XBee64BitAddress.from_hex_string(GND_ADDR)

cansat = XBeeDevice(CANSAT_PORT, CANSAT_BAUD_RATE)
cansat.open()
cansat.set_pan_id(bytearray(PANID))
cansat.set_dest_address(REMOTE64ADDR)

gnd = RemoteXBeeDevice(cansat, REMOTE64ADDR)


def runner():
	try:
		cansat.send_data(gnd, "HELLO")
	except Exception as e:
		print("Failed.")
		print(e)
		return False
	else:
		print("Success.")
		return True


if __name__ == "__main__":
	count = 5
	while count > 0:
		if runner():
			count = 0
		else:
			count -= 1
