from handcalcs.decorator import handcalc

@handcalc()
def compressive_strength(A: float = 1.0, fy: float = 355, gamma_M1: float = 1.0):
    N_Rd = A * fy / gamma_M1 

    return N_Rd

