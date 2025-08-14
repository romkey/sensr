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

# Setup I2C
i2c = busio.I2C(board.SCL, board.SDA)

while not i2c.try_lock():
    pass

print("Scanning I2C bus...")
devices = i2c.scan()
if devices:
    for device in devices:
        print(f"Found device at address: 0x{device:02X}")
else:
    print("No I2C devices found.")
i2c.unlock()

# Try to instantiate each sensor
scd40 = bme680 = tsl2591 = as7331 = None

try:
    if SCD4X:
        scd40 = SCD4X(i2c)
        scd40.start_periodic_measurement()
        print("SCD40 initialized.")
except Exception as e:
    print(f"SCD40 init failed: {e}")

try:
    if adafruit_bme680:
        bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
        bme680.sea_level_pressure = 1013.25
        print("BME680 initialized.")
except Exception as e:
    print(f"BME680 init failed: {e}")

try:
    if adafruit_tsl2591:
        tsl2591 = adafruit_tsl2591.TSL2591(i2c)
        print("TSL2591 initialized.")
except Exception as e:
    print(f"TSL2591 init failed: {e}")

try:
    if AS7331:
        as7331 = AS7331(i2c)
        print("AS7331 initialized.")
except Exception as e:
    print(f"AS7331 init failed: {e}")

# Main reporting loop
while True:
    print("\n--- Sensor Readings ---")

    if scd40 and scd40.data_ready:
        try:
            co2, temp, hum = scd40.measurement
            print(f"SCD40 - CO2: {co2:.1f} ppm, Temp: {temp:.2f} °C, Humidity: {hum:.2f} %")
        except Exception as e:
            print(f"SCD40 read failed: {e}")

    if bme680:
        try:
            print(f"BME680 - Temp: {bme680.temperature:.2f} °C, Humidity: {bme680.humidity:.2f} %, "
                  f"Pressure: {bme680.pressure:.2f} hPa, Gas: {bme680.gas:.1f} ohms")
        except Exception as e:
            print(f"BME680 read failed: {e}")

    if tsl2591:
        try:
            print(f"TSL2591 - Lux: {tsl2591.lux:.2f}, Visible: {tsl2591.visible}, IR: {tsl2591.infrared}")
        except Exception as e:
            print(f"TSL2591 read failed: {e}")

    if as7331:
        try:
            reading = as7331.take_single_measurement()
            print(f"AS7331 - UVA: {reading['uva']}, UVB: {reading['uvb']}, UVC: {reading['uvc']}, "
                  f"Temp: {reading['temperature_c']:.2f} °C")
        except Exception as e:
            print(f"AS7331 read failed: {e}")

    time.sleep(60)
