from aluno import Aluno

class Curso:
    def __init__(self, id, nome, duracao, vagas, nota_corte):
        self.__id = id
        self.__nome = nome
        self.__duracao = duracao
        self.__vagas = vagas
        self.__nota_corte = nota_corte
        self.__alunos = []

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def duracao(self):
        return self.__duracao

    @property
    def vagas(self):
        return self.__vagas

    @property
    def nota_corte(self):
        return self.__nota_corte

    @property
    def alunos(self):
        return self.__alunos
    
    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)

    def reduzir_vagas(self, num):
        self.__vagas -= num

    def aumentar_vagas(self, num):
        self.__vagas += num

    def retirar_aluno(self, aluno):
        del self.__alunos[self.__alunos.index(aluno)]
        self.aumentar_vagas(1)

    def cadastrar_aluno(self, aluno):
        if type(aluno) != Aluno:
            print('A instância não é do tipo Aluno!')
            return False
        elif self.__vagas  == 0:
            print('Curso sem vagas!')
            return False
        else:
            self.adicionar_aluno(aluno)
            self.reduzir_vagas(1)
            print('Aluno adicionado!')
            return True

    def __str__(self):
        return f'{self.__alunos}'