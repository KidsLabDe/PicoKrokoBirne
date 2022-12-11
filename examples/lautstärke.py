import time
import board
import analogio
from board import *

from digitalio import DigitalInOut, Direction, Pull




from rainbowio import colorwheel
import neopixel

pixel_pin = board.GP12
num_pixels = 1

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
PURPLE = (180, 0, 255)


switch = DigitalInOut(board.GP0)
switch.direction = Direction.INPUT
switch.pull = Pull.DOWN



while True:
    noiseLevel = 0;
    for x in range(100000):
        if switch.value:
            noiseLevel = noiseLevel +1
    
    print("noiseLevel: ",noiseLevel)


    if noiseLevel < 500:
        pixels.fill(GREEN)
    elif noiseLevel < 1500:
        pixels.fill(YELLOW)
    elif noiseLevel < 4000:
        pixels.fill(RED)
    else:
        pixels.fill(PURPLE)
    
    pixels.show()       
    
