#!/usr/bin/python

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

def main():
    # Initialize Library
    disp.begin()

    # Get display width and height.
    width = disp.width
    height = disp.height

    # Clear display
    disp.clear()
    disp.display()

if __name__ == "__main__":
        main()
