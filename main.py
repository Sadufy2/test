import threading
import time
import board
import neopixel

npixel = 6
strip = neopixel.NeoPixel(board.D21, npixel)
speed = 0.1

off = (0, 0, 0)

strip[0] = (0, 255, 0)
time.sleep(3)
