#Curso - Lógica de Programação para Data Science e AI com Python
#Exercício 001
# Faça um programa que realize a cotação da moeda local X por uma moeda Y, usar como valor padrão 3.45

valorCotacao = 3.45

valor = float(input("Informe quanto você deseja converter: "))
conversao = valor * valorCotacao
print("Você terá que pagar:  R$", conversao, "para adquirir $", valor, "dollars")