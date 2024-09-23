'''
    CRIE UM PROGRAMA QUE:
    Solicite 5 número do tipo Float;
    Em cada número da lista deve informar;
    1º A raiz quadrada;
    2º Se a raiz quadrada é um valor do tipo int ou float.
'''
import math

lista_numeros = []

for i in range(5):
    entrada_numero = float(input(f"Digite aqui o {i + 1} número: "))
    lista_numeros.append(entrada_numero)
#--

for numero in lista_numeros:
    raiz_quadrada = math.sqrt(numero)

    if raiz_quadrada.is_integer():
        print(f'A raiz quadrada do {numero} é do valor {raiz_quadrada:.2f}, e é do tipo [ int ]')
    else:
        print(f'A raiz quadrada do {numero}  do valor {raiz_quadrada:.2f}, e é do tipo [ float ]')
    #--
#--

print("********** PROGRAMA FINALIZADO ********")