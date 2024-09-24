'''
    O programa deve receber 5 números;
    A entrada deve ser crescente, caso contrário, deve solicitar que insira novamente outro número na ordem crescente.
'''

numeros = []

while len(numeros) < 5:
    entrada_numeros = int(input("Digite um número: "))
    if len(numeros) == 0 or entrada_numeros > numeros[-1]:
        numeros.append(entrada_numeros)
    else:
        print(f"O número deve ser maior que o último número inserido!")
    #--
#--

print(f"Os números da lista em ordem crescente são: {numeros}")
