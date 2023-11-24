"""
Original Authors of Tcl Scripts  : 
    Silvia Mazzoni, 2006
Tcl Script Translation to Python :
    elastropy.com, 2023
Purpose : 
    Generate incremental displacements for Dmax.
    
    Args:
    Dmax: Peak displacement (can be + or negative).
    DincrStatic: Displacement increment (default=0.01, independently of units).
    CycleType: Type of displacement cycle, Push (0->+peak), Half (0->+peak->0), Full (0->+peak->0->-peak->0) (optional, def=Full).
    Fact: Scaling factor (optional, default=1).

    Returns:
    iDstep: Numpy array of displacement increments.
"""
# ===========================================================================
# Import Libraries
# ===========================================================================
import numpy as np


# ===========================================================================
# Main Code
# ===========================================================================

def GeneratePeaks(Dmax, DincrStatic=0.01, CycleType="Full", Fact=1):
    """
    Generate incremental displacements for Dmax.
    
    Args:
    Dmax: Peak displacement (can be + or negative).
    DincrStatic: Displacement increment (default=0.01, independently of units).
    CycleType: Type of displacement cycle, Push (0->+peak), Half (0->+peak->0), Full (0->+peak->0->-peak->0) (optional, def=Full).
    Fact: Scaling factor (optional, default=1).

    Returns:
    iDstep: Numpy array of displacement increments.
    """

    # Generate incremental displacements for Dmax
    Disp = 0.0
    iDstep = [0.0, 0.0]

    # Scale value
    Dmax *= Fact

    # Determine displacement increment direction
    if Dmax < 0:
        dx = -DincrStatic
    else:
        dx = DincrStatic

    NstepsPeak = int(abs(Dmax) / DincrStatic)

    # Generate incremental displacements
    # Note - 
    #    We used underscore ( _ ) as an iterator variable in a for-loop, because here the value of the
    #    iterator variable is not important, we just to repeat the for-loop NstepsPeak times.
    for _ in range(NstepsPeak):
        Disp += dx
        iDstep.append(Disp)

    # Handle different cycle types
    if CycleType != "Push":
        for _ in range(NstepsPeak):
            Disp -= dx
            iDstep.append(Disp)

        if CycleType != "Half":
            for _ in range(NstepsPeak):
                Disp -= dx
                iDstep.append(Disp)

            for _ in range(NstepsPeak):
                Disp += dx
                iDstep.append(Disp)

    # Convert the list to a Numpy array
    iDstep = np.array(iDstep)

    return iDstep

# Example usage:
# Dmax = 2.0
# DincrStatic = 0.02
# CycleType = "Full"
# Fact = 1.5

# result = GeneratePeaks(Dmax, DincrStatic, CycleType, Fact)
# print(result)

