# MODULARIZAR DADOS DE LEITURA
# NOME
def lerNome():
    while True:
        try:            
            nome = input('Nome: ')
            if len(nome) < 2:
                print('Nome inválido!')
            else:
                return nome
        except Exception as erroExcecao:
            print(f'Erro de exceção: {erroExcecao}')

# NOTA DO PRIMEIRO BIMESTRE
def lerNotaB1():
    while True:
        try:            
            notaB1 = float(input('Digite a nota do primeiro bimestre: '))
            if notaB1 < 0 or notaB1 > 10:
                print('Nota Inválida!')
            else:
                return notaB1
        except Exception as erroExcecao:
            print(f'Erro de exceção: {erroExcecao}')

# NOTA DO SEGUNDO BIMESTRE
def lerNotaB2():
    while True:
        try:            
            notaB2 = float(input('Digite a nota do segundo bimestre: '))
            if notaB2 < 0 or notaB2 > 10:
                print('Nota Inválida!')
            else:
                return notaB2
        except Exception as erroExcecao:
            print(f'Erro de exceção: {erroExcecao}')
   
#  LISTAR ALUNOS
def listagemAlunos(turma):
    for i, aluno in enumerate(turma, start=1):
        print(f'{i} - {aluno[0]}')

# MOSTRAR APROVADOS (CONSIDERANDO MEDIA = 6):
def aprovados(turma):
    aprovados = []
    for i in turma:
        if i[3] >= 6:
            aprovados.append(i)
    for j, nome in enumerate(aprovados):
        print(f'{j+1} - {nome[0]}')

# MOSTRAR REPROVADOS (CONSIDERANDO MEDIA = 6):
def reprovados(turma):
    reprovados = []
    for i in turma:
        if i[3] <= 6:
            reprovados.append(i)
    for j, nome in enumerate(reprovados):
        print(f'{j+1} - {nome[0]}')