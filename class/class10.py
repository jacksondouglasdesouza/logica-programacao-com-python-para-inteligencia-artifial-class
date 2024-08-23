#Curso - Lógica de Programação para Data Science e AI com Python
#Exercício 010

# O programa deve ler o valor total do serviço prestado de manutenção;
# O programa deve ler o percentual de impostos de serviços a serem pagos pela empresa;
# O programa deve ler o percentual de impostos de produtos a serem pagos pela empresa;
# O programa deve imprimir o total a ser pago nos dois impostos;
# - O valor que sobra de lucro após os descontos.

valueTotalServicos = float(input("Digite o valor total do serviço prestado: "))
valueImpostoServico = float(input("Digite o percentual a ser pago de imposto de serviço: "))
valueImpostoProduto = float(input("Digite o percentual a ser pago de imposto de produto: "))

pagarImpostoServicos = (valueTotalServicos / 100) * valueImpostoServico
pagarImpostoProdutos = (valueTotalServicos / 100) * valueImpostoProduto
lucro = valueTotalServicos - (pagarImpostoServicos + pagarImpostoProdutos)

print("Você deve pagar: R$", pagarImpostoServicos, "de imposto sobre serviços.")
print("Você deve pagar: R$", pagarImpostoProdutos, "de imposto sobre produto.")
print("Você terá um lucro de: R$", lucro)
