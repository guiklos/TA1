import pandas as pd
import numpy as np
from numpy import genfromtxt
import math
import os

print("Teste da Uniformidade para os GNP Inedito.\n")
print(' H0: Os valores observados têm distribuição Uniforme.')
print(' H1: Os valores observados não têm distribuição Uniforme.\n')


def Uniformidade():
    arquivoNum = open("GERALEO2.txt", "r")

    dados = genfromtxt(arquivoNum, delimiter=",")

    dadosFrame = pd.DataFrame(columns=[
        'Li', 'Ls', 'Fo', 'pi', 'G(x)', 'F(x)', '|F(x) - G(x)|'])

    dadosFrame['Li'] = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    dadosFrame['Ls'] = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'Fo'] = np.count_nonzero(
            (dadosFrame['Li'][index] <= dados) & (dadosFrame['Ls'][index] > dados))
        dadosFrame.loc[index, 'Fe'] = 60000000

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'pi'] = dadosFrame['Fo'][index]/len(dados)

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'G(x)'] = dadosFrame.loc[:index, 'pi'].sum()

    dadosFrame['F(x)'] = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, '|F(x) - G(x)|'] = abs(dadosFrame['F(x)']
                                                     [index] - dadosFrame['G(x)'][index])

    ksCalculado = dadosFrame['|F(x) - G(x)|'].max()
    ks5 = 1.36/math.sqrt(len(dados))

    print(" KS - Calculado: {0:.5f}\n"
          " KS - 5%: {1:.5f}".format(ksCalculado, ks5))

    if ks5 > ksCalculado:
        print(" Aceita-se H0.")
    else:
        print(" Rejeita-se H0.")


Uniformidade()
os.system("pause")
