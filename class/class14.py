# Imprimir os 10 primeiros números maiores que 50

for i in range(50, 61):
    print(i)
#--




# Crie um Programa que faça a leitura de 5 números Inteiros, depois faça a soma dos números e imprima do console.

soma = 0

for i in range(1, 6):
    value = int(input(f'Digite o {i}º. número: '))
    soma += value
#--

print(f'A soma dos 5 números é: {soma}')




# Crie uma tabuada emoldurada

value_tabuada = int(input('Digite o valor da tabuada: '))

print("_______________")
for i in range(1, 11):
    print(f'| {value_tabuada} x {i} = {value_tabuada * i} |')
#--
print("_______________")