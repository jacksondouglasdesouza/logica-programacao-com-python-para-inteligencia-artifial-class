#Curso - Lógica de Programação para Data Science e AI com Python
#Exercício 009

# O sistema deve ler o salário anual do usuário.
# O sistema deve calcular quanto o funcionário deve receber por mês.

salarioAnualUsuario = float(input("Digite o seu salário Anual: "))
salarioMensal = salarioAnualUsuario / 12

print("Você irá reber: R$", salarioMensal, "Por mês.")
