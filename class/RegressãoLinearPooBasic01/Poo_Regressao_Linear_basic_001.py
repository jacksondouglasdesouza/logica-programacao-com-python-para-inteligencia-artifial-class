# Regressão Linear Simples - Class 01

'''
    # FUNÇÃO DE CORRELAÇÃO (r):

    r = coeficiente de correlação
    cov = covariância
    var = variância

    Fórmula:
    r = cov(x, y) / math.sqrt(var(x) * var(y))

---------------------------------

    # FUNÇÃO DE INCLINAÇÃO (m):

    m = coeficiente angular (inclinação)
    S = desvio padrão

    Fórmula:
    m = r * (S(y) / S(x))

---------------------------------

    # FUNÇÃO DE INTERCEPTAÇÃO (b):

    b = interceptação (coeficiente linear)

    Ȳ = média de y
    X̄ = média de x
    m = inclinação

    Fórmula:
    b = Ȳ - (X̄ * m)

---------------------------------

    # FUNÇÃO DE PREVISÃO (P):

    P = previsão
    b = interceptação
    m = inclinação
    v = valor da variável independente (a ser analisada)

    Fórmula:
    P = b + (m * v)

'''

from numpy import *
import math

def correlacao(x, y):
    covariacao = cov(x, y, bias=True)[0][1]
    variancia_x = var(x)
    variancia_y = var(y)
    return covariacao / math.sqrt(variancia_x * variancia_y)
#--

def inclinacao(x, y, correlacao):
    stdx = std(x)
    stdy = std(y)
    return correlacao * (stdy / stdx)
#--

def interceptacao(x, y, inclinacao):
    media_x = mean(x)
    media_y = mean(y)-0
    return media_y - inclinacao * media_x
#--

def previsao(interceptacao, inclinacao, variavel_independente):
    return interceptacao + (inclinacao * variavel_independente)
#--

