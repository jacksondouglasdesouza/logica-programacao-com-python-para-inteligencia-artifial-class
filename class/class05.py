#Curso - Lógica de Programação para Data Science e AI com Python
#Exercício 005

#O programa deve receber o número total de alunos da escola;
#O programa deve ler a entrada do número de alunos do sexo masculino;
#O programa deve apresentar o valor em percentual de alunos do sexo masculino e do sexo feminino.


valordeAlunosdaEscola = int(input('Digite o valor total do aluno da escola: '))
valorDeMasculino = int(input('Digite o valor total do alunos do sexo Maculino: '))
valorDeFemininos = valordeAlunosdaEscola - valorDeMasculino

print("O total de alunos da escola é de: ", valordeAlunosdaEscola)
print("O valor de alunos do sexo masculino é de: ", valorDeMasculino)
print("O valor de alunos do sexo feminino é de: ", valorDeFemininos)

#-- VALORES PERCENTUAIS
''
percentualMasculino = valorDeMasculino * 100 / valordeAlunosdaEscola
percentualFeminino = valorDeFemininos * 100 / valordeAlunosdaEscola


print("O percentual de alunos do sexo masculino é de: ", percentualMasculino, "%")
print("---------------------------------------------")
print("O percentual de alunos do sexo feminino é de: ", percentualFeminino, "%")


