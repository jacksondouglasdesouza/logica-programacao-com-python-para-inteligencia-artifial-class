'''
    Escreva um programa que receba 10 valores inteiros;
    Os valores devem ser maiores que 0;
    imprima a média dos valores.
'''


'''
# VERSÃO 01 - SEM PACOTE DE STATISTIC

numeros_entrada = []
soma = 0

while len(numeros_entrada) < 10:
    numeros = int(input("Digite um número inteiro: "))

    if numeros > 0:
        numeros_entrada.append(numeros)
    else:
        print("Não é permitido esse valor, tente novamente")
    #--
#--

soma = sum(numeros_entrada)
quantidade = len(numeros_entrada)
media = soma / quantidade


print(f'A média aritmética é de: {media}')
print(f'A soma dos números é de: {soma}')
print(f'A quantidade de números inseridos foi de: {quantidade}')

'''


# VERSÃO 02 - COM PACOTE DE STATISTIC

from  statistics import mean

entrada_dados = []

while len(entrada_dados) < 10:
    numero = int(input("Digite um valor inteiro: "))

    if numero > 0:
        entrada_dados.append(numero)
    else:
        print("Valor digitado não permitido! Tente novamente")
    #--
#--

media = mean(entrada_dados)
soma = sum(entrada_dados)
media_Manual = int( soma / len(entrada_dados))

#--

print(f'A soma dos números inseridos foi de: {soma}')
print(f'A média com a função [ mean() ] é de: {media}')
print(f'A média manual é de: {media_Manual}')