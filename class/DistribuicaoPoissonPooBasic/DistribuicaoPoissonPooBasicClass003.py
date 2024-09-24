# Distribuição de Poisson - POO Basic - Class 003
"""
Distribuição de Poisson:

- Mede a probabilidade da ocorrência de eventos em intervalo de tempo.
- Os eventos a cada intervalo devem ser independentes.

Fórmula:

P(X = x) = (e^(-λ) * λ^x) / x!

- x = número de eventos que estão sendo calculados.
- λ = número médio de eventos que ocorre por intervalo.
- e = constante de euler = 2,71828.

Exemplo 1:

O número de acidentes de carros que ocorrem por dia é de 2 acidentes.
Qual a probabilidade de ocorrerem 3 acidentes em um determinado dia?

Dado:

- X = 3
- λ = 2

Cálculo:

P(X = 3) = (2,71828^(-2) * 2^3) / 3!
P(X = 3) = (0,13533555 * 8) / 6
P(X = 3) ≈ 0,1804

"""

import math
from math import pow, factorial


def poisson(numero_eventos_x, lambda_value):
    return pow(math.e, -lambda_value) * pow(lambda_value, numero_eventos_x) / factorial(numero_eventos_x)
#--

print(f"A probabilidade de ocorrerem 3 acidentes dado que a média é e 2 acidentes por dia é: {poisson(2,2)}")



