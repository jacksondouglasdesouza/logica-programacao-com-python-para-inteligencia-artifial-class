#Class - Orientação a Objetos em Python

class aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
    #--

    def matricular(self):
        print(f'O aluno(a) {self.nome} de Matrícula {self.matricula} do curso de {self.curso}, foi matriculado com sucesso!')
    #--
#--

jackson= aluno('Jackson Douglas de Souza', 1528647563258, 'Engenharia Mecatrônica')


print("ENTRADA DE DADOS DO ALUNO: ")
print(f'O Nome completo do Aluno é: {jackson.nome}')
print(f'A Matrícula do Aluno é: {jackson.matricula}')
print(f'O Curso do Aluno é: {jackson.curso}')

print("\n*********************************************************************\n")
print("RETORNO DA SECRETARIA:\n")
jackson.matricular()
print("\n*********************************************************************\n")