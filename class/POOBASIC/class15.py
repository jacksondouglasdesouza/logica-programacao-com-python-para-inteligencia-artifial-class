'''
Exercício 1: Calculadora de Média

O programa deve calcular a média de dois números informados pelo usuário.
Os números devem ser informados como parâmetros da função.
A função deve retornar o cálculo.
O programa que chamar a função deve imprimir o resultado.

'''

def calculaMeida(a, b):
    media = (a + b) / 2
    return media
#--

value01 = float(input('Digite um valor: '))
value02 = float(input('Digite outro valor: '))

print(f'A média aritmética entre os valores {value01} e {value02} é de: {calculaMeida(value01, value02):.2f}')

#--


'''
Exercício 2: Impressão de Intervalo

Crie uma função que solicite a entrada de dois números inteiros.
O função deve imprimir o intervalo dos números informados:
Primeiramente em ordem crescente.
Em seguida, em ordem decrescente.
Faça uma chamada à função para testá-la.

'''

print("\n")

def imprimeIntervalo(a, b):
    if a == b:
        print("Intervalo Vazio!")
    else:
        # Ordem crescente
        print(f'Valores entre {a} e {b} em ordem crescente:')
        for i in range(min(a, b), max(a, b) + 1):
            print(i, end=" ")
        #--

        print("\n***************\n")

        # Ordem decrescente
        print(f'Valores entre {a} e {b} em ordem decrescente:')
        for i in range(max(a, b), min(a, b) - 1, -1):
            print(i, end=" ")
        #--

        print("\n***************\n")
    #--
#--

imprimeIntervalo(100, 20)
