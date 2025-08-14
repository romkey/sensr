# Sensr Base Board

The base board includes a CPU, two independently powered I2C busses and Qwiic ports, and an integrated accelerometer, header for a display and PMS5003 connector.

The current version is 0.2. Info on 0.1 is [here](base-board-0.1.md).

Because [JLCPCB apparently cannot correctly assemble boards with MEMS microphones](https://www.reddit.com/r/electronics/comments/1jy9k0o/warning_jlcpcb_cannot_reliably_handle_mems/) the board has a connector for an IMP451 microphone breakout instead of having an integrated MEMS microphone.

## 0.2 Pinout

| Name | Pin | Function |
|-----|-----|-------|
|SCL1|36
|SDA1|35
|SCL2|38
|SDA2|37|I2C2/Qwiic 2
|PM SET|41|Particle Sensor SET
|PM RX|40|Particle Sensor RX
|PM TX|39|Particle Sensor TX
|LED|45|Built in LED - low to light
|MIC_DAT|48|I2S Microphone Output
|MIC_CLK|47|I2S Microphone Clock
|MIC_WS|21|I2S Microphone Word Select
|ACC_INT|14|Accelerometer Interrupt
|SDO|9
|SDI|12
|SCK|11
|CS|9
|DCRS|3
|DSP_RST|46
|BCKLT|17
|T_CLK|7
|T_CS|6
|T_DO|5
|T_IRQ|4

## Firmware

### CircuitPython

https://circuitpython.org/board/yd_esp32_s3_n16r8/

#### Sound Level/Microphone

As of CircuitPython 9, it does not support I2S microphone input, so it is not possible to monitor sound levels from CircuitPython.

### EspHome
