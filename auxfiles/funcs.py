"""
Auxiliary functions to be used on the main file
"""
import numpy as np

T = np.arange(10000., 60000., 0.3)
# T = hc/(lamda*kB)
f = 1.4388e07
lamb = f / T  # nm


def gaussian(x, A, u, width):
    """
    gaussian(x, A, u, width) = A exp(-1/2 (x - u)**2/width**2)
    """
    return(
        A * np.exp(-1. / 2 * ((x - u) / width) ** 2)
    )


def lorentzian(x, peak, w, intens):
    return intens / (((peak - x) * 2. / w) ** 2 + 1.)


def addLor(excitationLvs, groundLvs, width, intens):
    spectrum = 0
    for enLv in excitationLvs:
        transitions = f / (enLv - groundLvs)
        spectrum += sum(
            [lorentzian(lamb, trans, width, intens) for trans in transitions]
        )
    return spectrum
