class Aluno:
    def __init__(self, cpf, nome, dt_nasc, pont_enem, matricula_uni_publica = False, matricula_uni_priv = False):
        self.__cpf = cpf
        self.__nome = nome
        self.__dt_nasc = dt_nasc
        self.__pont_enem = pont_enem
        self.__matricula_un_publica = matricula_uni_publica
        self.__matricula_un_priv = matricula_uni_priv

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def dt_nasc(self):
        return self.__dt_nasc

    @property
    def pont_enem(self):
        return self.__pont_enem

    @property
    def matricula_un_publica(self):
        return self.__matricula_un_publica

    @property
    def matricula_un_priv(self):
        return self.__matricula_un_priv
    
    def buscar_curso(self, universidade, curso):
        if curso in universidade.cursos:
            print('Há esse curso na universidade!')
            return True
        else:
            print('Não há esse curso na universidade')
            return False
        
    def verificar_nota(self, universidade, curso):
        if self.pont_enem >= universidade.cursos[universidade.cursos.index(curso)].nota_corte:
            print('Possui nota para o curso!')
            return True
        else:
            print('Não possui nota para o curso!')
            return False
        
    def solicitar_entrada(self, universidade, curso):
        return self.buscar_curso(universidade, curso) and self.verificar_nota(universidade, curso)
    
    def verificar_matriculas(self, universidade):
        if universidade.tipo == 'Pública':
            if self.matricula_un_publica:
                print('Já está matriculado em uma universidade pública!')
                return True
            else:
                print('Ainda não está matriculado em nenhuma universidade pública!')
                return False
            
    def tornar_se_matriculado_publica(self, universidade, curso):
        if universidade.cursos[universidade.cursos.index(curso)].cadastrar_aluno(self):
            self.__matricula_un_publica = True

    def tornar_se_matriculado_privada(self, universidade, curso):
        if universidade.cursos[universidade.cursos.index(curso)].cadastrar_aluno(self):
            self.__matricula_un_priv = True

    def efetivar_matricula(self, universidade, curso):
        if self.solicitar_entrada(universidade, curso):
            if universidade.tipo == 'Pública':
                if not self.verificar_matriculas(universidade):
                    self.tornar_se_matriculado_privada(universidade, curso)
            else:
                self.tornar_se_matriculado_publica(universidade, curso)

    def verificar_matricula(self, uni_origem, curso_origem):
        if self in uni_origem.cursos[uni_origem.cursos.index(curso_origem)].alunos:
            print('Matriculado na universidade!')
            return True
        else:
            print('Não está matriculado na universidade!')
            return False
        
    def verificar_vagas(self, curso_origem, uni_destino):
        if uni_destino.cursos[uni_destino.cursos.index(uni_destino.curso_igual(curso_origem))].vagas != 0:
            print('Ainda há vagas no curso!')
            return True
        else:
            print('Não há mais vagas no curso!')
            return False
        
    def desmatricular_se(self, universidade, curso):
        universidade.cursos[universidade.cursos.index(curso)].retirar_aluno(self)
        
    def solicitar_transferencia(self, uni_origem, curso_origem, uni_destino):
        if self.verificar_matricula(uni_origem, curso_origem):
            if self.verificar_vagas(curso_origem, uni_destino):
                if uni_destino.tipo == 'Pública':
                    if not self.verificar_matriculas(uni_destino):
                        self.desmatricular_se(uni_origem, curso_origem)
                        self.tornar_se_matriculado_publica(uni_destino, uni_destino.curso_igual(curso_origem))
                else:
                    self.desmatricular_se(uni_origem, curso_origem)
                    self.tornar_se_matriculado_privada(uni_destino, uni_destino.curso_igual(curso_origem))