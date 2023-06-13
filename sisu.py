from universidade import *

class Sisu:
    __universidades = []

    @staticmethod
    def incluir_universidade(universidade):
        if type(universidade) != Universidade:
            print('A instância não é do tipo Universidade!')
        else:
            Sisu.__universidades.append(universidade)
            print('Universidade adicionada!')