# Sensr Base Board 0.1.1

The base board includes a CPU, two independently powered I2C busses and Qwiic ports, and an integrated LSM6DS3TR-C accelerometer/gyroscope, header for a display and PMS5003 connector.

This board several severe defects. While some of them can be worked around in software it is not suitable for production and only later generation boards should be used.

## DEFECTS - IMPORTANT

1. capacitors on D+ and D- USB lines need to be removed or USB will not work correctly

2. PSRAM pins are used with the integrated I2S microphone and some of the display header pins
You can either use the connectors or you can use PSRAM. If you want to use the connectors be sure to install firmware that does not enable PSRAM. If you do, best case you won't be able to run I2C on the connectors, worst case your firmware will crash. 

3. The display header incorrectly connected - both SDO and SDI are wired to the same pin. Recommend not connecting SDO (MISO) on display boards.

4. The integrated I2S microphone will not work, even with PSRAM disabled. Apparently [JLCPCB apparently cannot correctly assemble boards with MEMS microphones](https://www.reddit.com/r/electronics/comments/1jy9k0o/warning_jlcpcb_cannot_reliably_handle_mems/)

5. The built-in LED on pin 45 does not work

## Pinout

| Name | Pin | Function |
|-----|-----|-------|
|SCL1|42|Qwiic1 SCL
|SDA1|41|Qwiic1 SDA
|SCL2|1|Qwiic2 SCL
|SDA2|2|Qwiic2 SDA
|PM SET|40|Particle Sensor SET
|PM RX|39|Particle Sensor RX
|PM TX|38|Particle Sensor TX
|LED|45|Built in LED - low to light
|MIC_DAT|48|I2S Microphone Output
|MIC_CLK|47|I2S Microphone Clock
|MIC_WS|35|I2S Microphone Word Select
|ACC_INT|36|Accelerometer Interrupt
|SDO|16
|SDI|16| MISTAKE - both SDO and SDI were sent to the same pin
|SCK|18
|CS|10
|DCRS|46
|DSP_RST|9
|BCKLT|17
|T_CLK|15
|T_CS|7
|T_DO|5
|T_IRQ|4
