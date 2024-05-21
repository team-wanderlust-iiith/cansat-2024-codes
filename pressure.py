from smbus2 import SMBus
import struct
import time

bus = SMBus(1)
bus.write_byte_data(0x77,0x1B,0x13)

while bus.read_byte_data(0x77,0x03) & 0x60 != 0x60:
	time.sleep(0.002)

data = bus.read_i2c_block_data(0x77,0x04,6)

adc_p = data[2] << 16 | data[1] << 8 | data[0]
adc_t = data[5] << 16 | data[4] << 8 | data[3]

coeff = bus.read_i2c_block_data(0x77,0x31,21)
#print (coeff)
coeff = bytes(coeff)
#print (coeff)
coeff = struct.unpack("<HHbhhbbHHbbhbb", coeff)

#print (coeff)

T1 = coeff[0] / 2**-8.0
T2 = coeff[1] / 2**30.0
T3 = coeff[2] / 2**48.0

P1 = (coeff[3] - 2**14.0) / 2**20.0
P2 = (coeff[4] - 2**14.0) / 2**29.0
P3 = coeff[5] / 2**32.0
P4 = coeff[6] / 2**37.0
P5 = coeff[7] / 2**-3.0
P6 = coeff[8] / 2**6.0
P7 = coeff[9] / 2**8.0
P8 = coeff[10] / 2**15.0
P9 = coeff[11] / 2**48.0
P10 = coeff[12] / 2**48.0
P11 = coeff[13] / 2**65.0

pd1 = adc_t - T1
pd2 = pd1 * T2

temperature = pd2 + (pd1 * pd1) * T3

pd1 = P6 * temperature
pd2 = P7 * temperature**2.0
pd3 = P8 * temperature**3.0
po1 = P5 +  pd1 + pd2 + pd3

pd1 = P2 * temperature
pd2 = P3 * temperature**2.0
pd3 = P4 * temperature**3.0
po2 = adc_p * (P1 +  pd1 + pd2 + pd3)

pd1 = adc_p**2.0
pd2 = P9 + P10 * temperature
pd3 = pd1 * pd2
pd4 = pd3 + P11 * adc_p**3.0

pressure = po1 + po2 + pd4
pressure = pressure / 100

sea_level_pressure = 935.92 #1013.25
altitude = 44307.7*(1-(pressure/sea_level_pressure)**0.190284)

print (temperature)
print (pressure)
print (altitude)
