"""
Original Authors of Tcl Scripts  : 
    Silvia Mazzoni & Frank McKenna, 2006
Tcl Script Translation to Python :
    elastropy.com, 2023
Purpose : 
    LibMaterialsRC.py contains material definitions to model RC members
"""


# ===========================================================================
# Import Libraries
# ===========================================================================
import openseespy.opensees as os
import math as mt
from LibUnits import *

# ===========================================================================
# Main Code
# ===========================================================================
# General Material parameters
G   = Ubig		    # make stiff shear modulus
J   = 1.0			# torsional section stiffness (G makes GJ large)
GJ  = G*J

# ---------------------------------------------------------------------------
# Confined and unconfined concrete
# ---------------------------------------------------------------------------

# nominal concrete compressive strength
fc  = -4.0*ksi		    # CONCRETE Compressive Strength, ksi   (+Tension, -Compression)
Ec  = 57*ksi*mt.sqrt(-fc/psi)	# Concrete Elastic Modulus
nu  =  0.2
Gc  = Ec/2./(1+nu)  	# Torsional stiffness Modulus

# confined concrete
Kfc     = 1.3			# ratio of confined to unconfined concrete strength
Kres    = 0.2			# ratio of residual/ultimate to maximum stress
fc1C    = Kfc*fc		# CONFINED concrete (mander model), maximum stress
eps1C   = 2.*fc1C/Ec	# strain at maximum stress 
fc2C    = Kres*fc1C		# ultimate stress
eps2C   = 20*eps1C		# strain at ultimate stress 
Lambda  = 0.1			# ratio between unloading slope at eps2 and initial slope Ec

# unconfined concrete
fc1U    =  fc			# UNCONFINED concrete (todeschini parabolic model), maximum stress
eps1U   = -0.003		# strain at maximum strength of unconfined concrete
fc2U    = Kres*fc1U		# ultimate stress
eps2U   = -0.01			# strain at ultimate stress

# tensile-strength properties
ftC     = -0.14*fc1C	# tensile strength +tension
ftU     = -0.14*fc1U	# tensile strength +tension
Ets     = ftU/0.002     # tension softening stiffness

IDconcCore  = 1
IDconcCover = 2


os.uniaxialMaterial('Concrete02', IDconcCore,  fc1C, eps1C, fc2C, eps2C, Lambda, ftC, Ets)
os.uniaxialMaterial('Concrete02', IDconcCover, fc1U, eps1U, fc2U, eps2U, Lambda, ftU, Ets)

# ---------------------------------------------------------------------------
# Reinforcing Steel
# ---------------------------------------------------------------------------
Fy  = 66.8*ksi		# steel yield stress
Es  = 29000.*ksi	# modulus of steel
Bs  = 0.01			# strain-hardening ratio 
R0  = 18			# control the transition from elastic to plastic branches
cR1 = 0.925			# control the transition from elastic to plastic branches
cR2 = 0.15			# control the transition from elastic to plastic branches

IDSteel = 3
os.uniaxialMaterial('Steel02', IDSteel, Fy, Es, Bs, R0, cR1, cR2)