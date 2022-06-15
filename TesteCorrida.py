import pandas as pd
import numpy as np
from numpy import genfromtxt
import math
import os

print("Teste das Corridas para os GNP Inedito.\n")
print(' H0: As corridas observadas não diferem das esperadas.')
print(' H1: As corridas observadas diferem das esperadas.\n')


def CorridaAsc():
    print(" Corrida Ascendente.")
    arquivoNum = open("GERALEO2.txt", "r")

    dados = genfromtxt(arquivoNum, delimiter=",")

    corrida = []
    corridaCount = 1

    x = 0

    while(x != len(dados)):
        if x == len(dados) - 1:
            corrida.append((corridaCount))
            break
        if dados[x] < dados[x + 1]:
            x = x + 1
            corridaCount = corridaCount + 1
        else:
            corrida.append((corridaCount))
            corridaCount = 1
            x = x + 2

    dadosFrame = pd.DataFrame(columns=[
        'Corrida Asc', 'Fo', 'pi', 'G(x)', 'f(x)', 'F(x)', '|F(x) - G(x)|'])

    dadosFrame['Corrida Asc'] = np.arange(1, (np.max(corrida) + 1), 1)

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'Fo'] = corrida.count(
            dadosFrame['Corrida Asc'][index])

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'pi'] = dadosFrame['Fo'][index] / \
            dadosFrame['Fo'].sum()

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'G(x)'] = dadosFrame.loc[:index, 'pi'].sum()

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'f(x)'] = dadosFrame['Corrida Asc'][index] / \
            math.factorial(dadosFrame['Corrida Asc'][index] + 1)

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
        print(' Aceita-se H0.')
    else:
        print(' Rejeita-se H0.')


def CorridaDesc():
    print("\n Corrida Descendente.")
    arquivoNum = open("GERALEO2.txt", "r")

    dados = genfromtxt(arquivoNum, delimiter=",")

    corrida = []
    corridaCount = 1

    x = 0

    while(x != len(dados)):
        if x == len(dados) - 1:
            corrida.append((corridaCount))
            break
        if dados[x] > dados[x + 1]:
            x = x + 1
            corridaCount = corridaCount + 1
        else:
            corrida.append((corridaCount))
            corridaCount = 1
            x = x + 2

    dadosFrame = pd.DataFrame(columns=[
        'Corrida Desc', 'Fo', 'pi', 'G(x)', 'f(x)', 'F(x)', '|F(x) - G(x)|'])

    dadosFrame['Corrida Desc'] = np.arange(1, (np.max(corrida) + 1), 1)

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'Fo'] = corrida.count(
            dadosFrame['Corrida Desc'][index])

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'pi'] = dadosFrame['Fo'][index] / \
            dadosFrame['Fo'].sum()

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'G(x)'] = dadosFrame.loc[:index, 'pi'].sum()

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'f(x)'] = dadosFrame['Corrida Desc'][index] / \
            math.factorial(dadosFrame['Corrida Desc'][index] + 1)

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
        print(" Aceita-se a hipótese H0.")
    else:
        print(" Rejeita-se a hipótese H0.")


CorridaAsc()
CorridaDesc()
os.system("pause")
