# Sensr

Sensr is an ESP32 S3-based microcontroller intended for environmental sensing, as well as separate sensor boards.

The base board includes:
- ESP32-S3 with 8MB of PSRAM and 16MB of flash storage
- USB C
- accelerometer
- I2S microphone
- connector for PMS5003 particle sensor
- 2 independent STEMMA QT/Qwiic connectors for external I2C boards
- 3 independent voltage regulators (CPU and STEMMA QT/Qwiic connectors)
- LED
- BOOT and RESET buttons
- display header

The Air sensor board includes:
- Bosch BME680 temperature/humidity/pressure/VOC sensor
- Sensirion SCD40 CO2 sensor

The Light sensor board includes:
- TSL25911 light/lux/infrared sensor
- AS7331 UVA/UVB/UVC sensor


## I2C Addresses

0x29 TSL25911
0x74 AS7331
0x49 AS7341
0x53 LT-390 

0x76 BME680
0x62 SCD40
0x59 SGP40
0x5D SFA30
0x44 SHT3X-D

0x6A LSM6DS3TR-C 

Gas:
0x64
0x65
0x66
0x67
0x68
0x69
0x6B


# bodged I2S
SCK - CS - 10
SD - RESET - 9
WS - DC - 46
L/R - SDI (MOSI) - 16
