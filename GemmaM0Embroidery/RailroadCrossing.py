# import libraries
import board
import digitalio
import neopixel
import time

# set up NeoPixels
NeoPixelPIN = board.D1
NUMPIXELS = 2
pixels = neopixel.NeoPixel(NeoPixelPIN, NUMPIXELS)

# Set up snap switch
SnapPIN = board.D2
Snap = digitalio.DigitalInOut(SnapPIN)
Snap.direction = digitalio.Direction.INPUT
Snap.pull = digitalio.Pull.UP

# initial state of the flasher
LitPixel = 0

# Forever loop
while True:
    # turn both pixels off
    pixels.fill((0, 0, 0))
    # is snap closed?
    if not Snap.value:
        # Snap closed: train comming, start / continue flashing
        # turn on the current pixel to full red
        pixels[LitPixel] = (255, 0, 0)
        # Set up for next time: select the other pixel
        LitPixel = (LitPixel + 1) % NUMPIXELS
    # Show the pixels
    pixels.show()
    # Sleep for 1 second
    time.sleep(1)