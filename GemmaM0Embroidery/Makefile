##-*- makefile -*-############################################################
#
#  System        : 
#  Module        : 
#  Object Name   : $RCSfile$
#  Revision      : $Revision$
#  Date          : $Date$
#  Author        : $Author$
#  Created By    : Robert Heller
#  Created       : Wed Apr 2 14:10:16 2025
#  Last Modified : <250522.1102>
#
#  Description	
#
#  Notes
#
#  History
#	
#  $Log$
#
##############################################################################
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
##############################################################################


all: ClassSlides.pdf ClassNotes.pdf

ClassSlides.pdf: ClassSlides.tex ../rphpartpage.sty ClassSlides.d RailroadCrossing.py
	-rm -f ClassSlides.pdf ClassSlides.toc ClassSlides.snm ClassSlides.out ClassSlides.nav ClassSlides.aux ClassSlides.log
	pdflatex ClassSlides.tex
	pdflatex ClassSlides.tex
	pdflatex ClassSlides.tex


ClassSlides.d: ImageDeps.tcl ClassSlides.tex 
	echo "ClassSlides.pdf: \\" > ClassSlides.d
	tclsh ImageDeps.tcl ClassSlides.tex >> ClassSlides.d
	echo "" >> ClassSlides.d
	
-include ClassSlides.d

ClassNotes.pdf: ClassNotes.tex ClassNotes.d RailroadCrossing.py
	-rm -f ClassNotes.pdf ClassNotes.toc ClassNotes.aux ClassNotes.log
	pdflatex ClassNotes.tex
	pdflatex ClassNotes.tex
	pdflatex ClassNotes.tex
	pdflatex ClassNotes.tex

ClassNotes.d: ImageDeps.tcl ClassNotes.tex
	echo "ClassNotes.pdf: \\" > ClassNotes.d
	tclsh ImageDeps.tcl ClassNotes.tex >> ClassNotes.d
	echo "" >> ClassNotes.d
	
-include ClassNotes.d

%.png: %.jpg
	convert $< $@

ClearNailPolish.png: ClearNailPolish.jpeg
	convert $< $@
