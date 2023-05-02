import threading
import time
import board
import neopixel
import random

npixel = 6
strip = neopixel.NeoPixel(board.D21, npixel)
speed = 0.1

off = (0, 0, 0)

def Blink(idx):
    for i in range(0, 30):
        strip[idx] = (0, 0, 100)
        time.sleep(random.randint(1, 10)/10)
        strip[idx] = off
        time.sleep(random.randint(1, 10)/10)

t0 = threading.Thread(target=Blink, args=(0,))
t1 = threading.Thread(target=Blink, args=(1,))

t0.start()
t1.start()

strip.fill(off)
