# TFT SPI Displays

## SDO/MISO Defect

https://github.com/Bodmer/TFT_eSPI/discussions/898

Some ST7796 and ILI9488 displays have a superfluous diode on the chip select line. This prevents the SDO/MISO pin (the only output pin on the display) from going tristate when the display isn't selected. To fix the display, remove the diode or simply do not connect the pin.

ILI9488 displays have this defect and cannot be fixed. On these displays you must not connect the SDO/MISO pin if you will have any other devices on the same SPI bus.

