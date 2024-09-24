# Atividade 01

'''
    Solicite 5 nomes ao usuário;
    O programa não deve se importar com a forma de entrada de dados do usuário, se é ou não maiúscula ou minúscula;
    O programa deve apresentar no prompt os nomes de entrada com sua primeira letra em maiúscula.
'''

nomes = []

while len(nomes) != 5:
    entrada_nomes = input("Digite aqui o nome: ").capitalize()
    nomes.append(entrada_nomes)
#--
print(f"""
    Os nomes digitados são:
    {nomes}\n
""")


#--

nomes = []

# Receber nomes do usuário
while len(nomes) < 5:  # Mudado para < 5 para facilitar a contagem
    faltam = 5 - len(nomes)  # Calcula quantos nomes faltam
    entrada_nomes = input(f"Digite aqui o nome (faltam {faltam} nomes): ").capitalize()
    nomes.append(entrada_nomes)

# Exibir os nomes digitados
print(f"""
    Os nomes digitados são:
    {nomes}
""")
