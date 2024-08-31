# Curso - Lógica de Programação para Data Science e AI com Python
# Estruturas de Repetição

count = 1

while count <= 5:
    print(count)
    count += 1
#--

print(" ")

for n in range(1, 11):
    print(n)
#--

# EXERCÍCIO

'''
    Crie um programa que leia a idade do cliente
    - A idade deve ser um valor igual ou maior que zero;
    - Se não atender este critério, o programa deve solicitar novamente a entrada;
    - Se atendida, finaliza o laço.
'''

idade_usuario = 0

while idade_usuario >= 0:
    idade_usuario = int(input("Digite sua idade: "))

    if idade_usuario >= 18:
        print("Sua idade é válida para o processo seletivo!")
        print("Legal, você já está preparado para concorrer a vaga!")
        break
    elif idade_usuario < 18 and idade_usuario > 0:
        print("Idade é inválida para o processo seletivo!")
        print("Tente novamente!")
    elif idade_usuario < 0:
        print("Não existe sua idade!")
        print("Programa Finalizado!")
        break
    #--
#--


validador = False

while validador == False:
    value01 = int(input("Digite um valor inteiro: "))
    value02 = int(input("Digite outro valor inteiro: "))

    if (value01 > 0 and value02 > 0) and (value01 < value02):
        validador = True
    #--
#--

print("Progressão: ")

for i in range(value01, value02 + 1):
    print(i)
#--

print(" Regressão: ")

for j in range(value02, value01 - 1, -1):
    print(j)
#--


