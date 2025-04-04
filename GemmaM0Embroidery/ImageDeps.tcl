#*****************************************************************************
#
#  System        : 
#  Module        : 
#  Object Name   : $RCSfile$
#  Revision      : $Revision$
#  Date          : $Date$
#  Author        : $Author$
#  Created By    : Robert Heller
#  Created       : Fri Apr 4 12:31:06 2025
#  Last Modified : <250404.1245>
#
#  Description	
#
#  Notes
#
#  History
#	
#*****************************************************************************
## @copyright
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
# @file ImageDeps.tcl
# @author Robert Heller
# @date Fri Apr 4 12:31:06 2025
# 
#
#*****************************************************************************


package require snit

snit::type ExtractIncludedImages {
    pragma -hastypeinfo    no
    pragma -hastypedestroy no
    pragma -hasinstances   no
    
    typevariable PATTERN {\\includegraphics[^{]*\{([^}]*)\}(.*)$}
    
    typeconstructor {
        #puts stderr "*** PATTERN is '$PATTERN'"
        set infile [lindex $::argv 0]
        set fp [open $infile r]
        while {[gets $fp line ] >= 0} {
            set buffer $line
            #puts stderr "*** buffer is '$buffer'"
            while {[regexp $PATTERN $buffer => image rest] > 0} {
                puts stdout "\t$image \\"
                set buffer $rest
                #puts stderr "*** buffer is '$buffer'"
            }
        }
        close $fp
    }
}


