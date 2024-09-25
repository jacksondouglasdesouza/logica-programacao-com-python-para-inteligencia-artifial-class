import numpy as np
from sklearn.linear_model import LinearRegression

quantidade_variaveis = int(input("Informe a quantidade de variáveis para o modelo:  "))

variaveis_dependentes_y = []
variaveis_independentes_x = []

print("Informe os valores para as", quantidade_variaveis, "variáveis dependentes Y: ")

for indice in range(quantidade_variaveis):
    valor_dependente_y = int(input(f"Informe o valor da variável dependente {indice + 1}: "))
    variaveis_dependentes_y.append(valor_dependente_y)
#--

print("Informe os valores para as", quantidade_variaveis, "variáveis independentes x: ")

for indice in range(quantidade_variaveis):
    valor_independente_x = int(input(f"Informe o valor da variável independente {indice + 1}: "))
    variaveis_independentes_x.append(valor_independente_x)
#--

valor_para_prever = int(input("Informe o valor da variável independente que deseja prever: "))

variaveis_independentes_x = np.array(variaveis_independentes_x).reshape(-1, 1)
variaveis_dependentes_y = np.array(variaveis_dependentes_y)

# Cria o modelo
modelo_regressao_linear = LinearRegression()

# Treina o modelo com os dados inseridos
modelo_regressao_linear.fit(variaveis_independentes_x, variaveis_dependentes_y)
valor_para_prever = np.array([[valor_para_prever]])

# Realiza a previsão usando o modelo treinado
resultado_previsao = modelo_regressao_linear.predict(valor_para_prever)

print("O Resultado da Previsão é:", resultado_previsao)

