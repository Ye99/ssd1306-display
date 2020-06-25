from machine import I2C, Pin
import ssd1306

i2c = I2C(-1, Pin(5), Pin(4))
# confirmed with i2c_scanner, display address is 0x3C, which is the default
display = ssd1306.SSD1306_I2C(128, 64, i2c)


display.text("1234567890123456", 0, 0)
display.text("2234567890123456", 0, 8)
display.text("3234567890123456", 0, 16)
display.text("4234567890123456", 0, 24)
display.text("5234567890123456", 0, 32)
display.text("6234567890123456", 0, 40)
display.text("7234567890123456", 0, 48)
display.text("8234567890123456", 0, 56)

"""
ICON = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 1, 1, 0, 0, 0, 1, 1, 0],
    [ 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [ 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0],
]

display.fill(0) # Clear the display
for y, row in enumerate(ICON):
    for x, c in enumerate(row):
        display.pixel(x, y, c)
"""

display.show()



