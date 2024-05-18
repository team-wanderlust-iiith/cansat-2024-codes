from smbus2 import SMBus #import SMBus module of I2C
from datetime import datetime, timedelta

# Some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47
TEMP_OUT     = 0x41
Device_Address = 0x69 #0x68

def init():
	# Setup
	bus = SMBus(1) # or bus = smbus.SMBus(0) for older version boards
	#Device_Address = 0x68 # MPU6050 device address

	#write to sample rate register
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

	#Write to power management register
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

	#Write to Configuration register
	bus.write_byte_data(Device_Address, CONFIG, 0)

	#Write to Gyro configuration register
	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

	#Write to interrupt enable register
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)


def read_raw_data(addr):
	# Setup
	init()
	bus = SMBus(1) # or bus = smbus.SMBus(0) for older version boards
	#Device_Address = 0x68 # MPU6050 device address

	# Accel and Gyro value are 16-bit
	high = bus.read_byte_data(Device_Address, addr)
	low = bus.read_byte_data(Device_Address, addr+1)

        # Concatenate higher and lower value
	value = ((high << 8) | low)

	# To get signed value from mpu6050
	if (value > 32768):
		value = value - 65536
	return value


def readAccX():
	acc_x = read_raw_data(ACCEL_XOUT_H)
	#Full scale range +/- 250 degree/C as per sensitivity scale factor
	Ax = acc_x/16384.0
	return Ax


def readAccY():
	acc_y = read_raw_data(ACCEL_YOUT_H)
	#Full scale range +/- 250 degree/C as per sensitivity scale factor
	Ay = acc_y/16384.0
	return Ay


def readAccZ():
	acc_z = read_raw_data(ACCEL_ZOUT_H)
	#Full scale range +/- 250 degree/C as per sensitivity scale factor
	Az = acc_z/16384.0
	return Az


def readGyroX():
	gyro_x = read_raw_data(GYRO_XOUT_H)
	#Full scale range +/- 250 degree/C as per sensitivity scale factor
	Gx = gyro_x/131.0
	return Gx


def readGyroY():
	gyro_y = read_raw_data(GYRO_YOUT_H)
	#Full scale range +/- 250 degree/C as per sensitivity scale factor
	Gy = gyro_y/131.0
	return Gy


def readGyroZ():
	gyro_z = read_raw_data(GYRO_ZOUT_H)
	#Full scale range +/- 250 degree/C as per sensitivity scale factor
	Gz = gyro_z/131.0
	return Gz


def readTemperature():
	temp = read_raw_data(TEMP_OUT)
	#Full scale range +/- 250 degree/C as per sensitivity scale factor
	T = (temp / 340) + 36.53
	return T


def readData():
	Ax = readAccX()
	Ay = readAccY()
	Az = readAccZ()

	Gx = readGyroX()
	Gy = readGyroY()
	Gz = readGyroZ()

	T = readTemperature()

	return [Ax, Ay, Az, Gx, Gy, Gz, T]


def testModule():
#	init()

	print (" Reading Data of Gyroscope, Accelerometer and Temperature")
	Ax, Ay, Az, Gx, Gy, Gz, T = readData()
	print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az, "\tTemperature=%.2f" %T)
#	print (f"Ax = {Ax}, Ay = {Ay}, Az = {Az}, Gx = {Gx}, Gy = {Gy}, Gz = {Gz}, T = {T}")


if __name__ == "__main__":
	time = datetime.now()
	while True:
		if (datetime.now() - time) >= timedelta(seconds = 1):
			time = datetime.now()
			testModule()
