'''
    Escreva um código que receba 10 valores inteiros;
    Imprima no console o maior e o menor número dentre os digitados.
'''

value_entrada = []

while len(value_entrada) < 10:
    numbers = int(input("Digite um valor: "))
    value_entrada.append(numbers)
#-

print(f'O menor valor digitado foi {min(value_entrada)}')
print(f"O maior valor digitado foi {max(value_entrada)}")

