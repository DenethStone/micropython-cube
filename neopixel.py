from microbit import *
import neopixel
from random import randint


# Setup the Neopixel strip on pin0 with a length of 8 pixels
np = neopixel.NeoPixel(pin0, 14)

def barva(r,g,b):
    for pixel_id in range(0, len(np)):
        red = r
        green = g
        blue = b

        # Assign the current LED a random red, green and blue value between 0 and 60
        np[pixel_id] = (red, green, blue)

        # Display the current pixel data on the Neopixel strip
        np.show()

while True:
    #Iterate over each LED in the strip
    barva(255,0,0) #cervena
    sleep(100)
    barva(0,255,0) #zelena
    sleep(100)
    barva(0,0,255) #modra
    sleep(100)
    barva(255,255,0) #žlutá
    sleep(100)
    barva(255,0,255) #růžová
    sleep(100)
    barva(0,255,255) #žlutá
    sleep(100)


