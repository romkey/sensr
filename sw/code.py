import time
import board
import busio

# Sensor libraries
try:
    from adafruit_scd4x import SCD4X
except ImportError:
    SCD4X = None

try:
    import adafruit_bme680
except ImportError:
    adafruit_bme680 = None

try:
    import adafruit_tsl2591
except ImportError:
    adafruit_tsl2591 = None

try:
    from as7331 import AS7331
except ImportError:
    AS7331 = None

try:
    from adafruit_pm25.uart import PM25_UART
except ImportError:
    PM25_UART = None

try:
    import adafruit_lsm6ds.lsm6ds3
except ImportError:
    adafruit_lsm6ds = None

# Setup I2C and UART
i2c = busio.I2C(board.IO42, board.IO41)

# PMS5003 uses UART (adjust pins as needed for your board)
uart = None
try:
    import busio as busio_uart
    uart = busio_uart.UART(board.IO39, board.IO38, baudrate=9600, timeout=0.25)
except Exception:
    pass

while not i2c.try_lock():
    pass

print("Scanning I2C bus...")
devices = i2c.scan()
if devices:
    for device in devices:
        print("Found device at address: 0x%02X" % device)
else:
    print("No I2C devices found.")
i2c.unlock()

# Sensor instances
scd40 = bme680 = tsl2591 = as7331 = pms5003 = lsm6ds = None

try:
    if SCD4X:
        scd40 = SCD4X(i2c)
        scd40.start_periodic_measurement()
        print("SCD40 initialized.")
except Exception as e:
    print("SCD40 init failed:", e)

try:
    if adafruit_bme680:
        bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, 0x76)
        bme680.sea_level_pressure = 1013.25
        print("BME680 initialized.")
except Exception as e:
    print("BME680 init failed:", e)

try:
    if adafruit_tsl2591:
        tsl2591 = adafruit_tsl2591.TSL2591(i2c)
        print("TSL2591 initialized.")
except Exception as e:
    print("TSL2591 init failed:", e)

try:
    if AS7331:
        as7331 = AS7331(i2c)
        print("AS7331 initialized.")
except Exception as e:
    print("AS7331 init failed:", e)

try:
    if uart and PM25_UART:
        pms5003 = PM25_UART(uart)
        print("PMS5003 initialized.")
except Exception as e:
    print("PMS5003 init failed:", e)

try:
    if adafruit_lsm6ds:
        lsm6ds = adafruit_lsm6ds.lsm6ds3.LSM6DS3(i2c)
        print("LSM6DS33 initialized.")
except Exception as e:
    print("LSM6DS33 init failed:", e)

# Main loop
while True:
    print("\n--- Sensor Readings ---")

    if scd40 and scd40.data_ready:
        try:
            print("SCD40 - CO2: %.1f ppm, Temp: %.2f C, Humidity: %.2f%%" % (
                scd40.CO2, scd40.temperature, scd40.relative_humidity))
        except Exception as e:
            print("SCD40 read failed:", e)

    if bme680:
        try:
            print("BME680 - Temp: %.2f C, Humidity: %.2f%%, Pressure: %.2f hPa, Gas: %.1f ohms" % (
                bme680.temperature, bme680.humidity, bme680.pressure, bme680.gas))
        except Exception as e:
            print("BME680 read failed:", e)

    if tsl2591:
        try:
            print("TSL2591 - Lux: %.2f, Visible: %d, IR: %d" % (
                tsl2591.lux, tsl2591.visible, tsl2591.infrared))
        except Exception as e:
            print("TSL2591 read failed:", e)

    if as7331:
        try:
            reading = as7331.take_single_measurement()
            print("AS7331 - UVA: %d, UVB: %d, UVC: %d, Temp: %.2f C" % (
                reading["uva"], reading["uvb"], reading["uvc"], reading["temperature_c"]))
        except Exception as e:
            print("AS7331 read failed:", e)

    if pms5003:
        try:
            data = pms5003.read()
            print("PMS5003 - PM1.0: %d µg/m3, PM2.5: %d µg/m3, PM10: %d µg/m3" % (
                data.pm10_standard, data.pm25_standard, data.pm100_standard))
        except Exception as e:
            print("PMS5003 read failed:", e)

    if lsm6ds:
        try:
            accel = lsm6ds.acceleration
            gyro = lsm6ds.gyro
            print("LSM6DS33 - Accel: (%.2f, %.2f, %.2f) m/s^2, Gyro: (%.2f, %.2f, %.2f) dps" % (
                accel[0], accel[1], accel[2], gyro[0], gyro[1], gyro[2]))
        except Exception as e:
            print("LSM6DS33 read failed:", e)

    time.sleep(10)
