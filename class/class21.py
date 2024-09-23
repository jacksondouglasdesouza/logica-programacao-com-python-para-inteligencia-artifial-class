"""
    Escreva um programa que:
    Receba 5 valores do usuário para 1º lista;
    Receba 5 valores do usuário para 2º lista;

    Informar ao usuário, se ouve coincid~encia de valores nas posições das listas, após a comparação.

"""

primeira_lista = []

print("Insira 5 valores para a 1ª lista: ")

for i in range(5):
    entrada_dados_01 = int(input(f"Digite o {i + 1}ª valor: "))
    primeira_lista.append(entrada_dados_01)
#--

segunda_lista = []

print("Insira 5 valores para a 2ª lista: ")

for i in range(5):
    entrada_dados_02 = int(input(f"Digite o {i + 1}ª valor: "))
    segunda_lista.append(entrada_dados_02)
#--

coincidencias = []

for i in range(5):
    if primeira_lista[i] == segunda_lista[i]:
        coincidencias.append((i + 1, primeira_lista[i]))
    #--
#--

if coincidencias:
    print("\nForam encontradas coincidências nas posições: \n")

    for posicao, valor in coincidencias:
        print(f"Posição {posicao}º : Valor [ {valor} ]")
    #--

else:
    print("Nenhuma coincidência foi encontrada nas posições.")
#--
