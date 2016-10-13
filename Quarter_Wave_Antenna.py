#!/usr/bin/env python

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

# PiVFO Version 0.1
# A GUI for freq_pi
# Jenny List G7CKF
# http://www.languagespy.com

import time
import math
import subprocess

#import and rename the 'tkinter' module for < Python 3.3:
import Tkinter as tkinter

#Initial frequency, variable then holds VFO frequency
vfoFreq = 14000000
#VFO state
vfoState = False

#Max frequency 250MHz
maxFreq = 250000000
#Min frequency is 125kHz
minFreq = 125000

#Location of freq_pi 
freqgen = "./freq_pi"

def doQuitEvent(key):
	c.resetty() # set terminal settings
	c.endwin()  # end curses session
	subprocess.call([freqgen, "-q"]) #Turn off the clock
	raise SystemExit

#VFO on and off
def vfoOnFunc():
	global vfoState
	subprocess.call([freqgen, "-f", str(vfoFreq)])
	vfoState = True
	vfoOnButton['state'] = 'disabled'
	vfoOffButton['state'] = 'normal'

def vfoOffFunc():
	global vfoState
	subprocess.call([freqgen, "-q"])
	vfoState = False
	vfoOnButton['state'] = 'normal'
	vfoOffButton['state'] = 'disabled'

#Change frequency
de