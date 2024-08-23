#Curso - Lógica de Programação para Data Science e AI com Python
#Exercício 008

#O programa deve ler o salário do funcionário em Float;
#O programa deve ler um percentual de reajuste em Float;
#O sistema deve imprimir no prompt de comando o salário reajustado.

salarioUsuario = float(input("Digite aqui o seu salário: "))
percentualReajuste = float(input("Digite o percentual de reajuste do seu salário: "))
salarioReajustado = ((salarioUsuario / 100) * percentualReajuste) + salarioUsuario

print("O seu salário reajustado é de: ", salarioReajustado)

