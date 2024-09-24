'''
    RECEBA 5 NÚMEROS;
    Armazene-os numa lista;
    Faça a leitura e imprima somente os números pares e informa a sua posição na lista.
'''

numeros = []


for i in range(5):
    entrada_numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(entrada_numero)
#--

print("Números pares e suas posições na lista: ")

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        print(f"Número {numeros[i]} na posição {i}ª da lista de números.")
    #--
#--