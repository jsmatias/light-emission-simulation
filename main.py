import pandas as pd
import matplotlib.pyplot as pl
import numpy as np
from auxfiles.funcs import *
import auxfiles.loader as ld
import inputArguments as args
import importlib

# importlib.reload(ld)
importlib.reload(args)
pd.options.mode.chained_assignment = None
pl.close('all')
pl.ion()

fileNamePath = './input/' + args.filePath
outputSpectraFile = './output/' + \
    args.filePath.split('/')[-1].split('.')[0] + 'spectra.csv'

dataObj = ld.LOADER(fileNamePath)
dataObj.CleanEnergy()
dataObj.CleanLSSqrd()
dataObj.GetS()
dataObj.GetL()

selectedEnLvs = dataObj.LevelsFromSpectra(args.energyLevels)

T = np.arange(10000., 60000., 0.3)
# T = hc/(lamda * kB)
f = 1.4388e07
lamb = f / T + args.displacement  # nm

spectra = 0
enLvsKeys = list(args.energyLevels.keys())
for i in range(len(args.energyLevels)):
    # All transitions to ground state: enLvsKeys[0]
    spectra += addLor(
        excitationLvs=selectedEnLvs[enLvsKeys[i]].energy,
        groundLvs=selectedEnLvs[enLvsKeys[0]].energy,
        width=args.energyLevels[enLvsKeys[i]][3],
        intens=args.energyLevels[enLvsKeys[i]][2]
    )

pd.DataFrame({
    'wavelength_nm': lamb,
    'intensity_au': spectra
}).to_csv(outputSpectraFile, index=False)

fig2 = pl.figure(1)
pl.plot(lamb, spectra)
pl.xlabel(r'$\lambda$ (nm)')
pl.ylabel('Intensity (a.u.)')
pl.xlim([500 + args.displacement, 700 + args.displacement])
pl.show()
fig2.savefig('./output/spectra.png')

dataObj.PlotLvs()
dataObj.ExportResults()
