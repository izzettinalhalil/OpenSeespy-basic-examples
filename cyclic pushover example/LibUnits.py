"""
Original Authors of Tcl Scripts  : 
    Silvia Mazzoni & Frank McKenna, 2006
Tcl Script Translation to Python :
    elastropy.com, 2023
Purpose : 
    LibUnits.py contains system of units that will be used in this simulation
"""


# ===========================================================================
# Import Libraries
# ===========================================================================
import math as mt


# ===========================================================================
# Main Code
# ===========================================================================

inch        = 1.0
kip         = 1.0
sec         = 1.0
LunitTXT    = "inch"
FunitTXT    = "kip"
TunitTXT    = "sec"			    # define basic-unit text for output
ft          = 12.0*inch 		# define engineering units
ksi         = kip/pow(inch,2)
psi         = ksi/1000.0
lbf         = psi*inch*inch		# pounds force
pcf         = lbf/pow(ft,3)		# pounds per cubic foot
psf         = lbf/pow(ft,3)		# pounds per square foot
in2         = inch*inch 		# inch^2
in4         = inch*inch*inch*inch 		# inch^4
cm          = inch/2.54		    # centimeter, needed for displacement input in MultipleSupport excitation
PI          = 2*mt.asin(1.0) 		# define constants
g           = 32.2*ft/pow(sec,2) 	# gravitational acceleration
Ubig        = 1.e10 			# a really large number
Usmall      = 1/Ubig 		    # a really small number
