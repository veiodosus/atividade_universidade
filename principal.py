from datetime import *
from sisu import *

"""CRIANDO ALUNOS"""
dt_nasc_1 = datetime(2000, 5, 18)
joao = Aluno('12345678901', 'João', dt_nasc_1, 600)
dt_nasc_2 = datetime(2001, 6, 12)
marcelo = Aluno('10987654321', 'Marcelo', dt_nasc_2, 700)
dt_nasc_3 = datetime(2003, 1, 29)
tiago = Aluno('11122233344', 'Tiago', dt_nasc_3, 500)
dt_nasc_4 = datetime(2002, 2, 19)
astolfo = Aluno('44433322211', 'Astolfo', dt_nasc_4, 900)
dt_nasc_5 = datetime(2004, 12, 12)
gilgamesh = Aluno('55566677788', 'Gilgamesh', dt_nasc_5, 600)
dt_nasc_6 = datetime(1999, 6, 6)
ticardo = Aluno('88877766655', 'Ticardo', dt_nasc_6, 800)
"""CRIANDO CURSOS"""
medicina = Curso(1, 'Medicina', 600, 20, 899)
engenharia = Curso(2, 'Engenharia', 550, 40, 799)
matematica = Curso(3, 'Matemática', 500, 60, 699)
biologia = Curso(4, 'Biologia', 600, 80, 599)
filosofia = Curso(5, 'Filosofia', 400, 100, 599)
artes = Curso(6, 'Artes', 500, 40, 599)
# UFPI
ufpi_medicina = Curso(1, 'Medicina', 600, 20, 899)
ufpi_engenharia = Curso(2, 'Engenharia', 550, 40, 799)
ufpi_matematica = Curso(3, 'Matemática', 500, 60, 699)
ufpi_biologia = Curso(4, 'Biologia', 600, 80, 599)
# UNIP
unip_medicina = Curso(1, 'Medicina', 600, 20, 899)
unip_engenharia = Curso(2, 'Engenharia', 550, 40, 799)
unip_matematica = Curso(3, 'Matemática', 500, 60, 699)
unip_biologia = Curso(4, 'Biologia', 600, 80, 599)
# UFB
ufb_matematica = Curso(3, 'Matemática', 500, 60, 699)
ufb_biologia = Curso(4, 'Biologia', 600, 80, 599)
ufb_filosofia = Curso(5, 'Filosofia', 400, 100, 599)
ufb_artes = Curso(6, 'Artes', 500, 40, 599)
# HVD
hvd_matematica = Curso(3, 'Matemática', 500, 60, 699)
hvd_biologia = Curso(4, 'Biologia', 600, 80, 599)
hvd_filosofia = Curso(5, 'Filosofia', 400, 100, 599)
hvd_artes = Curso(6, 'Artes', 500, 40, 599)
"""CRIANDO UNIVERSIDADES"""
ufpi = Universidade('UFPI', 'Universidade Federal do Piauí', 'Pública')
unip = Universidade('UNIP', 'Universidade Privada', 'Privada')
ufb = Universidade('UFB', 'Universidade Federal de Brasília', 'Pública')
hvd = Universidade('HVD', 'Havardi', 'Privada')
"""TESTANDO CADASTRAMENTO DE ALUNOS CUJO TIPO ESTÁ ERRADO"""
ufpi.cadastrar_curso("a")
print('')
"""ADICIONANDO CURSOS NAS UNIVERSIDADES - 1"""
ufpi.cadastrar_curso(ufpi_medicina)
ufpi.cadastrar_curso(ufpi_engenharia)
ufpi.cadastrar_curso(ufpi_matematica)
ufpi.cadastrar_curso(ufpi_biologia)
"""ADICIONANDO CURSOS NAS UNIVERSIDADES - 2"""
unip.cadastrar_curso(unip_medicina)
unip.cadastrar_curso(unip_engenharia)
unip.cadastrar_curso(unip_matematica)
unip.cadastrar_curso(unip_biologia)
"""ADICIONANDO CURSOS NAS UNIVERSIDADES - 3"""
ufb.cadastrar_curso(ufb_matematica)
ufb.cadastrar_curso(ufb_biologia)
ufb.cadastrar_curso(ufb_filosofia)
ufb.cadastrar_curso(ufb_artes)
"""ADICIONANDO CURSOS NAS UNIVERSIDADES - 4"""
hvd.cadastrar_curso(hvd_matematica)
hvd.cadastrar_curso(hvd_biologia)
hvd.cadastrar_curso(hvd_filosofia)
hvd.cadastrar_curso(hvd_artes)
print('')
"""ADICIONANDO UNIVERSIDADES NO SISU"""
Sisu.incluir_universidade(ufpi)
Sisu.incluir_universidade(unip)
Sisu.incluir_universidade(ufb)
Sisu.incluir_universidade(hvd)
print('')
"""TESTANDO INCLUSÃO DE UNIVERSIDADE CUJO TIPI ESTÁ ERRADO"""
Sisu.incluir_universidade('a')
print('')
"""TESTANDO BUSCA DE CURSO PELOS ALUNOS"""
joao.buscar_curso(ufpi, artes) # False
marcelo.buscar_curso(unip, unip_medicina) # True
tiago.buscar_curso(ufb, engenharia) # False
astolfo.buscar_curso(ufb, ufb_filosofia) # True
gilgamesh.buscar_curso(hvd, hvd_artes) # True
ticardo.buscar_curso(hvd, hvd_matematica) # True
print('')
"""TESTANDO VERIFICAÇÃO DE NOTA POR ALUNOS"""
joao.verificar_nota(unip, unip_medicina) # False
marcelo.verificar_nota(ufb, ufb_filosofia) # True
tiago.verificar_nota(hvd, hvd_artes) # False
astolfo.verificar_nota(hvd, hvd_matematica) # True
gilgamesh.verificar_nota(ufb, ufb_artes) # True
ticardo.verificar_nota(ufpi, ufpi_engenharia) # True
print('')
"""TESTANDO SOLICITAÇÃO DE ENTRADA POR ALUNOS"""
joao.solicitar_entrada(ufpi, ufpi_biologia) # True
marcelo.solicitar_entrada(unip, unip_medicina) # False
tiago.solicitar_entrada(hvd, hvd_artes) # False
astolfo.solicitar_entrada(ufb, engenharia) # False
gilgamesh.solicitar_entrada(hvd, hvd_filosofia) # True
ticardo.solicitar_entrada(unip, unip_medicina) # False
print('')
"""TESTANDO EFETIVAÇÃO DE MATRÍCULA"""
joao.efetivar_matricula(ufpi, ufpi_biologia)
joao.efetivar_matricula(hvd, hvd_biologia)
print('')
"""VERIFICANDO DECREMENTO NO NÚMERO DE VAGAS DOS CURSOS"""
print(ufpi.cursos[ufpi.cursos.index(ufpi_biologia)].vagas)
print(hvd.cursos[hvd.cursos.index(hvd_biologia)].vagas)
print('')
"""VERIFICANDO TRANSFERÊNCIA"""
joao.efetivar_matricula(hvd, hvd_filosofia)
joao.solicitar_transferencia(hvd, hvd_filosofia, ufb)
print('')
astolfo.efetivar_matricula(unip, unip_matematica)
astolfo.solicitar_transferencia(unip, unip_matematica, hvd)