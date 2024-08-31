value_tabuada = int(input("Digite o valor da tabuada: "))

for i in range(1,11):
    print(f'{value_tabuada} X {i} = {value_tabuada * i}')
#--


validador = True
while validador == True:
    value_tabuada = int(input("Digite o valor da tabuada: "))
    for i in range(1, 11):
        print(f'{value_tabuada} X {i} = {value_tabuada * i}')
    #--

    new_value_tabuada = input("Deseja continuar [S/N]? ")

    if new_value_tabuada.upper() == "N":
        validador = False
        print("Programa Finalizado com Sucesso!")
    #--
#--


