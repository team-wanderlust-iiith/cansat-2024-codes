from typing import List, Any
from ADS1115 import ADS1115_Sensor
from AHT21B import AHT21B_Sensor
from BMP390 import BMP390_Sensor
from DS3231 import DS3231_Sensor
from MPU6050 import MPU6050_Sensor
from MS4525DO import MS4525DO_Sensor


class Sensors:
	"""
	Class for all sensors combined.
	"""

	def _sensor_init(self):
		while True:
			try:
#				print("Initilising Sensors.")
				self._bmp390 = BMP390_Sensor()
				self._ads1115 = ADS1115_Sensor()
				self._aht21b = AHT21B_Sensor()
#				self._ds3231 = DS3231_Sensor()
				self._mpu6050 = MPU6050_Sensor()
				self._ms4525do = MS4525DO_Sensor()
			except:
				print("Error initialising. Trying again.")
			else:
				break


	def __init__(self) -> None:
		"""
		Class constructor. Initialises a :class:`Sensors` object,
		along with the appropriate sensor modules and values.
		"""
		self._sensor_init()
		# Sensor modules and individual values.
		## BMP390
#		self._bmp390 = BMP390_Sensor()
		self._bmp390_temperature: float = None
		self._bmp390_pressure: float = None
		self._bmp390_altitude: float = None
		## ADS1115
		self._ads1115 = ADS1115_Sensor()
		self._ads1115_voltage_channel_0: float = None
		self._ads1115_voltage_channel_1: float = None
		# self._ads1115_voltage: float = None
		## AHT21B
#		self._aht21b = AHT21B_Sensor()
		self._aht21b_temperature: float = None
		## DS3231
#		self._ds3231 = DS3231_Sensor()
		self._ds3231_raw_time: List[int] = None
		self._ds3231_telemetry_time: str = None
		## MPU6050
#		self._mpu6050 = MPU6050_Sensor()
		self._mpu6050_temperature: float = None
		self._mpu6050_acc_x: float = None
		self._mpu6050_acc_y: float = None
		self._mpu6050_acc_z: float = None
		self._mpu6050_gyro_x: float = None
		self._mpu6050_gyro_y: float = None
		self._mpu6050_gyro_z: float = None
		## MS4525DO
#		self._ms4525do = MS4525DO_Sensor()
		self._ms4525do_pressure: float = None
		self._ms4525do_air_speed: float = None
		pass ## Add other sensors

		# Data values.
		self.altitude: float = None
		self.air_speed: float = None
		self.temperature: float = None
		self.pressure: float = None
		self.voltage: float = None
		self.GPS_time: str = None
		self.GPS_altitude: float = None
		self.GPS_latitude: float = None
		self.GPS_longitude: float = None
		self.GPS_sats: int = None
		self.tilt_X: float = None
		self.tilt_Y: float = None
		self.telemetry_time: str = None
		self.rotation_Z: float = None
		self.optional_data: str = None

		return

	def _update_bmp390_values(self) -> List[float]:
		"""
		Function to update values from BMP390.

		Returns:
			`temperature`, `pressure`, `altitude` readings from BMP390.
		"""
		self._bmp390_temperature, self._bmp390_pressure, self._bmp390_altitude = self._bmp390.read_values()

		return self._bmp390_temperature, self._bmp390_pressure, self._bmp390_altitude

	def callibrate_base_pressure(self, base_pressure: float = None):
		return self._bmp390._set_base_pressure(base_pressure)

	def _update_ads1115_values(self) -> List[float]:
		"""
		Function to update values from ADS1115.

		Returns:
			`channel_0_voltage`, `channel_1_voltage` readings from ADS1115.
		"""
		self._ads1115_voltage_channel_0, self._ads1115_voltage_channel_1 = self._ads1115.read_values()

		return self._ads1115_voltage_channel_0, self._ads1115_voltage_channel_1

	def _update_aht21b_values(self) -> List[float]:
		"""
		Function to update temperature from AHT21B.

		Returns:
			`temperature` reading from AHT21B.
		"""
		self._aht21b_temperature = self._aht21b.read_value()

		return self._aht21b_temperature

	def _update_mpu6050_values(self) -> List[float]:
		"""
		Function to update values from MPU6050.

		Returns:
			`temperature` reading from MPU6050.
		"""
		[
			self._mpu6050_temperature,
			self._mpu6050_acc_x,
			self._mpu6050_acc_y,
			self._mpu6050_acc_z,
			self._mpu6050_gyro_x,
			self._mpu6050_gyro_y,
			self._mpu6050_gyro_z
		] = self._mpu6050.read_values()

		return [
			self._mpu6050_temperature,
			self._mpu6050_acc_x,
			self._mpu6050_acc_y,
			self._mpu6050_acc_z,
			self._mpu6050_gyro_x,
			self._mpu6050_gyro_y,
			self._mpu6050_gyro_z
		]

	def _update_ms4525do_values(self) -> List[float]:
		"""
		Function to update values from MS4525DO.

		Returns:
			`pressure`, `air_speed` readings from MS4525DO.
		"""
		self._ms4525do_pressure, self._ms4525do_air_speed = self._ms4525do.read_values()

		return self._ms4525do_pressure, self._ms4525do_air_speed

	def _update_ds3231_values(self) -> tuple[List[int], str]:
		"""
		Function to update values from DS3231.

		Returns:
			`raw_time`, `telemetry_time` readings from DS3231.
		"""
		self._ds3231_raw_time, self._ds3231_telemetry_time = self._ds3231.read_values()

		return self._ds3231_raw_time, self._ds3231_telemetry_time

	def _calc_pressure(self) -> float:
		pressure = self._bmp390_pressure/2 + self._ms4525do_pressure/2

		return pressure

	def _calc_temperature(self) -> float:
		temperature = self._aht21b_temperature/3 + self._bmp390_temperature/3 + self._mpu6050_temperature/3

#		return temperature
		return self._aht21b_temperature

	def _calc_voltage(self) -> float:
		return self._ads1115_voltage_channel_0 + self._ads1115_voltage_channel_1

	def update_sensor_values(self):
		try:
			self._update_ads1115_values()
			self._update_aht21b_values()
			self._update_bmp390_values()
#			self._update_ds3231_values()
			self._update_mpu6050_values()
			self._update_ms4525do_values()
		except:
			return False
		else:
			return True

	def update_values(self, update_raw=False):
		if update_raw:
			while not self.update_sensor_values():
				print("Trying to read again.")

		self.air_speed = self._ms4525do_air_speed
		self.altitude = self._bmp390_altitude
		# self.GPS_altitude
		# self.GPS_latitude
		# self.GPS_longitude
		# self.GPS_sats
		# self.GPS_time
		self.optional_data = ""
		self.pressure = self._calc_pressure()
		self.rotation_Z = self._mpu6050_gyro_z
		self.temperature = self._calc_temperature()
		self.telemetry_time = self._ds3231_telemetry_time
		self.tilt_X = self._mpu6050_gyro_x
		self.tilt_Y = self._mpu6050_gyro_y
		self.voltage = self._calc_voltage()

		return

	def read_values(self) -> list:
		return [
			self.altitude,
			self.air_speed,
			self.temperature,
			self.pressure,
			self.voltage,
			self.GPS_time,
			self.GPS_altitude,
			self.GPS_latitude,
			self.GPS_longitude,
			self.GPS_sats,
			self.tilt_X,
			self.tilt_Y,
			self.rotation_Z,
			self.telemetry_time,
			self.optional_data
		]

	def get_values(self, update_raw=False) -> list:
		self.update_values(update_raw)
		return self.read_values()
