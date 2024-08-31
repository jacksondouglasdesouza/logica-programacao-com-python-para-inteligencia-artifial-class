'''

quantidade_value = int(input("Quantos Números você irá usar: "))
soma = 0

for quantidade_value in range(1, quantidade_value + 1):
    texto = f'Informe o {str(quantidade_value)}º. número.'
    soma = soma + int(input(texto))
#--

media = soma / quantidade_value

print(f'A média geral é: {media}')

'''

quantidade_value = int(input("Quantos Números você irá usar: "))
soma = 0

for i in range(1, quantidade_value + 1):
    new_value = int(input(f'Digite o {i} número: '))
    soma = soma + new_value
#--

media = soma / quantidade_value

print(f'A média geral é: {media}')


