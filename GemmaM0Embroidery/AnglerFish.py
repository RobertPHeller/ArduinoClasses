#*****************************************************************************
#
#  System        : 
#  Module        : 
#  Object Name   : $RCSfile$
#  Revision      : $Revision$
#  Date          : $Date$
#  Author        : $Author$
#  Created By    : Robert Heller
#  Created       : Sun May 18 09:20:35 2025
#  Last Modified : <250518.0930>
#
#  Description	
#
#  Notes
#
#  History
#	
#*****************************************************************************
#
#    Copyright (C) 2025  Robert Heller D/B/A Deepwoods Software
#			51 Locke Hill Road
#			Wendell, MA 01379-9728
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
# 
#
#*****************************************************************************


# import libraries
import board
import digitalio
import neopixel
import time

# set up NeoPixels
NeoPixelPIN = board.D1
NUMPIXELS = 1
pixels = neopixel.NeoPixel(NeoPixelPIN, NUMPIXELS)

# Set up snap switch
SnapPIN = board.D2
Snap = digitalio.DigitalInOut(SnapPIN)
Snap.direction = digitalio.Direction.INPUT
Snap.pull = digitalio.Pull.UP

# Forever loop
while True:
    if not Snap.value:
        # Snap closed: set color to light blueish
        pixels[0] = (200, 211, 254)
        # Show the pixel
        pixels.show()
    else:
        # Snap open: set color to red
        pixels[0] = (250, 0, 0)
        # Show the pixel
        pixels.show()
    # sleep for 50 ms.
    time.sleep(.050)
