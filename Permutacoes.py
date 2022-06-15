import pandas as pd
import numpy as np
from numpy import genfromtxt
import math
import os

print("Teste das Permutações para os GNP Inedito.\n")
print(' H0: Os ordenamentos observados não diferem dos esperados.')
print(' H1: Os ordenamentos observados diferem dos esperados.\n')


def sequencia(a, b, c, d):
    if a > b and b > c and c > d:
        return 0
    if a > b and b > d and d > c:
        return 1
    if a > c and c > b and b > d:
        return 2
    if a > c and c > d and d > b:
        return 3
    if a > d and d > b and b > c:
        return 4
    if a > d and d > c and c > b:
        return 5
    if b > a and a > c and c > d:
        return 6
    if b > a and a > d and d > c:
        return 7
    if b > c and c > a and a > d:
        return 8
    if b > c and c > d and d > a:
        return 9
    if b > d and d > a and a > c:
        return 10
    if b > d and d > c and c > a:
        return 11
    if c > a and a > b and b > d:
        return 12
    if c > a and a > d and d > b:
        return 13
    if c > b and b > a and a > d:
        return 14
    if c > b and b > d and d > a:
        return 15
    if c > d and d > a and a > b:
        return 16
    if c > d and d > b and b > a:
        return 17
    if d > a and a > b and b > c:
        return 18
    if d > a and a > b and b > c:
        return 19
    if d > b and b > a and a > c:
        return 20
    if d > b and b > c and c > a:
        return 21
    if d > c and c > a and a > b:
        return 22
    if d > c and c > b and b > a:
        return 23


def Pemutacoes():
    arquivoNum = open("GERALEO2.txt", "r")

    dados = genfromtxt(arquivoNum, delimiter=",")

    permutacao = np.zeros(24)

    for x in range(4, len(dados) + 1, 4):
        index = sequencia(
            dados[x - 4], dados[x - 3], dados[x - 2], dados[x - 1])
        permutacao[index] = permutacao[index] + 1

    dadosFrame = pd.DataFrame(columns=[
        'Permutações', 'Fo', 'pi', 'G(x)', 'f(x)', 'F(x)', '|F(x) - G(x)|'])

    dadosFrame['Permutações'] = np.arange(1, 25, 1)

    dadosFrame['Fo'] = permutacao

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'pi'] = dadosFrame['Fo'][index] / \
            dadosFrame['Fo'].sum()

    for index, row in dadosFrame.iterrows():
        dadosFrame.loc[index, 'G(x)'] = dadosFrame.loc[:index, 'pi'].sum()

    dadosFrame['f(x)'] = 1 / 24

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


Pemutacoes()
os.system("pause")
