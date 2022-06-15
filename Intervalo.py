import pandas as pd
import numpy as np
from numpy import genfromtxt
import math
import os

print("Teste dos Intervalos para os GNP Inedito.")
digito = int(
    input('Informe qual o digito que deseja realizar o Teste do Intervalo: '))
print(
    '\n H0: Os intervalos observados para o digito {0} não diferem dos esperados.'.format(digito))
print(
    ' H1: Os intervalos observados para o digito {0} diferem dos esperados.\n'.format(digito))


def Intervalo():
    arquivoNum = open("GERALEO2.txt", "r")

    dados = genfromtxt(arquivoNum, delimiter=",")

    intervalo = []
    intervaloCount = 0
    x = 0

    digitoCal = str(digito)

    while(x != len(dados)):
        numero = str(dados[x]).split('.')[-1][0]

        if numero == digitoCal:
            intervalo.append(intervaloCount)
            intervaloCount = 0
            x = x + 1
        else:
            x = x + 1
            intervaloCount = intervaloCount + 1
        if x == len(dados):
            intervalo.append(intervaloCount)

    dadosFrame = pd.DataFrame(columns=[
        'Intervalo', 'Fo', 'pi', 'G(x)', 'f(x)', 'F(x)', '|F(x) - G(x)|'])

    dadosFrame['Intervalo'] = np.arange(0, (np.max(intervalo) + 1), 1)

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'Fo'] = intervalo.count(
            dadosFrame['Intervalo'][index])

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'pi'] = dadosFrame['Fo'][index] / \
            dadosFrame['Fo'].sum()

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'G(x)'] = dadosFrame.loc[:index, 'pi'].sum()

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'f(x)'] = (
            0.9 ** dadosFrame['Intervalo'][index]) * 0.1

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'F(x)'] = dadosFrame.loc[:index, 'f(x)'].sum()

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, '|F(x) - G(x)|'] = abs(dadosFrame['F(x)']
                                                     [index] - dadosFrame['G(x)'][index])

    ksCalculado = dadosFrame['|F(x) - G(x)|'].max()

    ks5 = 1.36 / math.sqrt(dadosFrame['Fo'].sum())

    print(" KS - Calculado: {0:.5f}\n"
          " KS - 5%: {1:.5f}".format(ksCalculado, ks5))

    if ks5 > ksCalculado:
        print(" Aceita-se H0.")
    else:
        print(" Rejeita-se H0.")


Intervalo()
os.system("pause")
