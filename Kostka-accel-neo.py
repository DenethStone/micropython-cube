from microbit import *
import neopixel

np = neopixel.NeoPixel(pin0, 14)
display.off()

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
    if accelerometer.was_gesture('up'):
        barva(255,0,0)
    if accelerometer.was_gesture('down'):
        barva(0,255,0)
    if accelerometer.was_gesture('left'):
        barva(0,0,255)
    if accelerometer.was_gesture('right'):
        barva(255,255,0)
    if accelerometer.was_gesture('face up'):
        barva(255,0,255)
    if accelerometer.was_gesture('face down'):
        barva(0,255,255)

