# Atividade 02

'''
    Crie um programa que o usuário informe a quantidade de número que irá inserir no input;
    O programa não deve aceitar menos de 2 números;
    Deve apresentar a soma do 1º e do último número informado;
    O produto do 1º pelo 2º número informado.
'''

valores = []

quantidade_valores = int(input("Informe a quantidade de números deseja inserir: "))

if quantidade_valores > 2:

    while len(valores) < quantidade_valores:
        entrada_valor = int(input("Digite um número: "))
        valores.append(entrada_valor)
    #--

    soma = valores[0] + valores[-1]
    produto = valores[0] * valores[1]

    print(" \n ")
    print(f"A soma de {valores[0]} com {valores[-1]} é: {soma}")
    print(f"O produto de {valores[0]} com {valores[1]} é: {produto}")

else:
    print("Não é possível a operação com valores abaixo de 2 números!")
#--