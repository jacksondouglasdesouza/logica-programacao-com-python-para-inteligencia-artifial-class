#Curso - Lógica de Programação para Data Science e AI com Python
#Exercício 003
# solicite 2 dados do tipo String de entrada para o usuário;
#Salve os valores recebidos nas variáveis Var1 e Var2;
#O sistema deve inverter os valores, colocando o valor de Var1 em Var2 e vice-versa;
# #O sistema deve imprimir o resultado das inversões.

Var1 = input("Digite a primeira String: ")
Var2 = input("Digite a segunda String: ")
VarAuxiliar = Var2

Var2 = Var1
Var1 = VarAuxiliar

print("Variável Var 01: ", Var1)
print("Variável Var 02:", Var2)
