from curso import *

class Universidade:
    def __init__(self, sigla, nome, tipo):
        self.__sigla = sigla
        self.__nome = nome
        self.__tipo = tipo
        self.__cursos = []

    @property
    def sigla(self):
        return self.__sigla
    
    @property
    def nome(self):
        return self.__sigla

    @property
    def tipo(self):
        return self.__tipo

    @property
    def cursos(self):
        return self.__cursos
    
    def adicionar(self, curso):
        self.__cursos.append(curso)

    def cadastrar_curso(self, curso):
        if type(curso) != Curso:
            print('A instância não é do tipo Curso!')
        else:
            self.adicionar(curso)
            print('Curso adicionado!')

    def curso_igual(self, curso):
        for n in self.__cursos:
            if curso.id == n.id:
                return n
    
    def __str__(self):
        return f'{self.__cursos}'