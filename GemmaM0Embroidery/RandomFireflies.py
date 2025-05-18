#*****************************************************************************
#
#  System        : 
#  Module        : 
#  Object Name   : $RCSfile$
#  Revision      : $Revision$
#  Date          : $Date$
#  Author        : $Author$
#  Created By    : Robert Heller
#  Created       : Sun May 18 09:32:05 2025
#  Last Modified : <250518.1707>
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
import neopixel
import random
import time

# set up NeoPixels
NeoPixelPIN = board.D1
NUMPIXELS = 4
pixels = neopixel.NeoPixel(NeoPixelPIN, NUMPIXELS)
# turn all pixels off
pixels.fill((0, 0, 0))
    
# Forever loop
while True:
    # pick a fly at random
    fly = random.randrange(0,NUMPIXELS)
    # light green
    pixels[fly] = (144, 238, 144)
    # Light him up
    pixels.show()
    time.sleep(0.5)
    # Back to darkness
    pixels[fly] = (0, 0, 0)
    pixels.show()
    time.sleep(1)
