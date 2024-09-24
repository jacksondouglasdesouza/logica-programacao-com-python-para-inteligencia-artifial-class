'''
    Crie uma lista com 10 nomes de usuários;
    Peça ao usuário um nome e cheque se este nome se encontra na lista;
    Informe ao usuário se o nome está ou não na lista.
    obs: O programa não deve ser case sensitive
'''


lista_nomes = ["João", "Carlos", "Silva", "Maria", "Luana", "Souza", "Débora", "Camila", "Douglas", "Fernando"]

nome_busca = input("Digite o nome para busca: ").strip().lower()

for i in range(len(lista_nomes)):
    print(f'[ {i}º ] : {lista_nomes[i]}')
    if nome_busca == lista_nomes[i].lower():
        print(f'\nO nome {nome_busca} foi encontrado na posição {i}º da lista')
        break
    #--
else:
    print("\nO nome não foi localizado na lista!")
#--

