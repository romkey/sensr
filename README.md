# Sensr

Sensr is a group of hardware projects intended for environmental
sensing.

It currently consists of:
- base board - ESP32-S3 with accelerometer, I2S microphone header, display header, 2 Qwiic ports, particle counter connector
- air - SCD40 CO2 + BME680 temperature/humidity/pressure sensor
- air-stcc4 - new STCC4 CO2 sensor + SHT40 temperature/humidity sensor
- light - TSL25911 light
- light-ltr390uv - LTR390 UV sensor + TSL25911 light sensor

Sensr is an ESP32 S3-based microcontroller intended for environmental sensing, as well as separate sensor boards.

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

## License

Hardware is shared under the [CERN-OHL-S-2.0](CERN_OHL_S_v2.txt) license.

Software is shared under the [MIT license](MIT-LICENSE.txt).

Documentation is shared under the [CC-BY-SA-4.0](CC-BY-SA-4.0.txt) - Attribution-ShareAlike license.

