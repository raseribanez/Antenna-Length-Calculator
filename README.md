# Antenna-Length-Calculator
A set of GUI programs - for calculating Radio Frequencies into Antenna Wavalength's

Written By Ben Woodfield (raserppsprograms@gmail.com)

Designed to be a simple tool for general antenna design across a wide range of frequencies.
A follow up version for each one will be compiled as .exe files - to cater for non-linux and non-python systems. 
(For Windows users without Python installed)

There are seperate versions for 1/4, 1/2, 5/8, and Full Loop.

You simply enter your desired frequency and the vertical wavelength by clicking either "Meters" or "Feet", depending on what
yourpreferences are. If you have a frequency range or band you wish to use, I would take the lowest frequency and highest frequency
for the range you want, and work out the average / mid-way point, then make adjustments from there.

NOTE this is just to get an idea of the wavelengths for specific frequencies - if used for Antenna design, you should know
that different frequencies(wavelengths) have different antenna systems that work better on some than others, 
e.g: I would make a dipole for the 1/2 wavelength at CB frequencies around 27 MHz, and use it as a vertical dipoole, 
not horizontal. 

If I used this calculator to find out the 1/2 wavelength of 27MHz, the result would then be spilt into 2 (halfed), the top section
would be my radiating element, and the lower half would be my ground (ground/lower element is connected to the braided/shielded outer COAX)

You will need Python 2 Installed to run these versions. 
Written on 2.7.9, also runs ok on 2.7.11.

The calculations used in the programs are below:

Vertical Antenna Calculations:

5/8 wave: (585 % MHz = feet), 5/8 wave: (178.3080 % MHz = mters)
1/2 wave: (468 % MHz = feet), 1/2 wave: (142.6464 % MHz = meters)
1/4 wave: (234 % MHz = feet), 1/4 wave: (71.3232 % MHz = mters)
Full Wave: (2005 % MHz = feet), full wave: (306.324 % MHz = meters

Feet to meters calculation

feet / 3.28 = meters
feet x 0.3048 = meters



Ben Woodfield
163-CT-160 - Charlie Tango
163-DR-663 - Delta Romeo
