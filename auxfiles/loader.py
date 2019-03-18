import pandas as pd
import numpy as np
import matplotlib.pyplot as pl


class LOADER():

    _fileName = ''
    __lSquared = np.array([1, 2, 6, 12, 20, 30, 42, 56])
    __sSquared = np.array([1.5, 3.5, 5.5, 7.5, 9.5, 11.5])
    _data = {}
    _selectedLvsDF = {}
    _selectedLvs = {}

    def __init__(self, fileName):
        '''
        '''
        self._data = pd.read_csv(
            fileName,
            sep='   ',
            skiprows=38,
            engine='python',
            header=None
        )
        self._fileName = fileName.split('/')[-1].split('.')[0]
        self._data.columns = ['energy', 'norma', 'l2', 's2', 'q', 'r', 'm']

    def data(self):
        '''
        '''
        return self._data

    def _cleanEnergy(self, cellStr):

        return float(cellStr.split(':')[1])

    def _cleanLSSqrd(self, cellStr):

        return float(cellStr.split(':')[2].split(',')[0].strip('('))

    def _getL(self, cellNumb):

        return(np.argmin(abs(self.__lSquared - cellNumb)))

    def _getS(self, cellNumb):

        return(np.argmin(abs(self.__sSquared - cellNumb)) + 0.5)

    def GetState(self, energyAndRange):

        filtre = abs(self._data.energy - energyAndRange[0]) < energyAndRange[1]
        stateDF = self._data[filtre]
        stateDF.loc[:, 'energyBased_J'] = len(
            stateDF) * [(len(stateDF) - 1) / 2]
        return stateDF

    def CleanEnergy(self):

        self._data.energy = self._data.energy.apply(self._cleanEnergy)

    def CleanLSSqrd(self):

        self._data.s2 = self._data.s2.apply(self._cleanLSSqrd)
        self._data.l2 = self._data.l2.apply(self._cleanLSSqrd)

    def GetS(self):

        self._data['s'] = self._data.s2.apply(self._getS)

    def GetL(self):

        self._data['l'] = self._data.l2.apply(self._getL)

    def LevelsFromSpectra(self, energyAndRange):

        for key in energyAndRange:
            self._selectedLvs[key] = self.GetState(energyAndRange[key])
            print('\n\t%s\n' % key, self._selectedLvs[key])
        print('''
            If the levels are not as expected, consider changing the input
            parameter in the inputArguments.py file.
        ''')
        self._selectedLvsDF = pd.concat(
            [self._selectedLvs[key] for key in self._selectedLvs.keys()]
        )
        return self._selectedLvs

    def PlotLvs(self, selectedLvs=True):
        fig1 = pl.figure(100)
        dataToPlot = \
            self._selectedLvsDF.energy if selectedLvs else self._data.energy
        for en in dataToPlot:
            pl.plot([0, 1], 2 * [en])

        if selectedLvs:
            for key in self._selectedLvs.keys():
                yPos = self._selectedLvs[key].energy.mean() + \
                    self._selectedLvs[key].energy.max() - \
                    self._selectedLvs[key].energy.min()
                pl.text(0.65, yPos, key, fontsize=10)

        pl.ylabel('Energy (K)')
        pl.show()
        fig1.savefig('./output/energyLvs.png')

    def ExportResults(self):
        outputFile = './output/' + self._fileName + '_energyLvs.csv'
        self._selectedLvsDF.to_csv(outputFile, index=False)
