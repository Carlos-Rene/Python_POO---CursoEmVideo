import rich
from ex002.pessoas import *


a1 = Aluno('José', 17, 'Informática', 'T01')
a1.fazer_matricula()
a1.fazer_aniversario()
#rich.inspect(a1, methods=True)

p1 = Professor('Guanabara', 43, 'Licenciatura', 'Pós-doutorado')
p1.fazer_aniversario()
p1.dar_aula()
#rich.inspect(p1, methods=True)

f1 = Funcionario('Claúdia', 27, 'Coordenadora', 'Coordenação')
f1.bater_ponto()
rich.inspect(f1)