#Curso - Lógica de Programação para Data Science e AI com Python
#Exercício 004

# O programa deve solicitar para o usuário um valor do tipo inteiro;
# O programa deve imprimir no console o que segue:
# O antecessor do número;
# O sucessor do número;
# A potência do Número.

valueEntrada = int(input("Digite um valor inteiro: "))

antecessor = valueEntrada - 1
sucessor = valueEntrada + 1
potencia = valueEntrada ** 2

print("O antecessor de : ", valueEntrada, "e: ", antecessor)
print("O sucessor de: ", valueEntrada, "e: ", sucessor)
print("A potência de: ", valueEntrada, "e: ", potencia)
