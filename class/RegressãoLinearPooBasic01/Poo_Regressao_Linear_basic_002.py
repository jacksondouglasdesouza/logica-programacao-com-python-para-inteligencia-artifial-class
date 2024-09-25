from Poo_Regressao_Linear_basic_001 import *

quantidade_dados = int(input("Informe a quantidade de variáveis do modelo: "))


variavel_dependente_y = []
for n in range(quantidade_dados):
    entrada_dados_y = int(input(f"Informe o valor da {n + 1}º variável dependente:  "))
    variavel_dependente_y.append(entrada_dados_y)
#--

variavel_independente_x = []

for n in range(quantidade_dados):
    entrada_dados_x = int(input(f"Informe o valor da {n + 1}º variável independente :  "))
    variavel_independente_x.append(entrada_dados_x)
#--

variavel_previsao = float(input("Informe o valor que deseja prever: "))

#--

variavel_correlacao = correlacao(variavel_independente_x, variavel_dependente_y)
variavel_inclinacao = inclinacao(variavel_independente_x, variavel_dependente_y, variavel_correlacao)
variavel_intercepcao = interceptacao(variavel_independente_x, variavel_dependente_y, variavel_inclinacao)
variavel_resultado = previsao(variavel_intercepcao, variavel_inclinacao, variavel_previsao)

#--

print(f"\nModelo de Regressão: ")
print(f"Correlação: {variavel_correlacao}")
print(f"Inclinação: {variavel_inclinacao}")
print(f"Interceptação: {variavel_intercepcao}")
print(f"Valor para prever: {variavel_previsao}")
print(f"Resultado da Previsão: {variavel_resultado}")
