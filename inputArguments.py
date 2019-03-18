"""
Change this file to change the input parameters
"""

# File name from energy levels simulation
# This file should be located in the input folder
filePath = 'Er_A4_-6888___A6_-0316079/ErenNaYF4_o9382_4'
# Er_A4_-823962__A6-3528/
# mesmo A4 e A6 316079
# ====================================================== #
#  Energy levels
# ====================================================== #
# Input:
# centre (Ei) of each energy state,
# a value lower than its approximate overall splitting (si),
# intensity of the transition to ground state (inti),
# and arbitrary width of the transition to the ground state (wi)
# Ex.:
# '4I15/2': (Ei, si, inti, wi)
energyLevels = {
    '4I15/2': (200, 1000, 0, 1),
    '4F9/2': (22000, 1000, 0.5, 7),
    '4S3/2': (26000, 1000, 1, 7),
    '4H11/2': (27000, 1000, 0.3, 7),
}

# displacement move the spectra on the x axis
displacement = 20  # nm
