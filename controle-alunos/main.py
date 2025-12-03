from alunos import lerNome, lerNotaB1, lerNotaB2, listagemAlunos, aprovados, reprovados
turma = []
# MENU
print('Menu Principal')
print('(1) Cadastrar aluno')
print('(2) Mostrar listagem de alunos')
print('(3) Mostrar aprovados')
print('(4) Mostrar Reprovados')
print('(0) Finalizar programa')

while True:
    try:
        opcao = int(input('Opção desejada: '))
        if opcao == 0:
            break

        # CADASTRO DE ALUNOS
        elif opcao == 1:            
            nome = lerNome() 
            notaB1 = lerNotaB1()  
            notaB2 = lerNotaB2()  
            media = (notaB1 + notaB2) / 2
            alunos = [nome, notaB1, notaB2, media]
            turma.append(alunos)
            print('Adicionado com sucesso!')

        # LISTAGEM DE TODOS OS ALUNOS
        elif opcao == 2:
            if len(turma) < 1:
                print('Não existem turmas.')
            else:  
                print('Lista de alunos: ')  
                lista = listagemAlunos(turma)

        # LISTAGEM DE APROVADOS
        elif opcao == 3:
            if len(turma) < 1:
                print('Não existem turmas.')
            else:    
                print('Lista de aprovados: ')
                listaAprovados = aprovados(turma)
                    
        # LISTAGEM DE REPROVADOS
        elif opcao == 4:
            if len(turma) < 1:
                print('Não existem turmas.')
            else:    
                print('Lista de reprovados: ')
                listaReprovados = reprovados(turma) 

    except Exception as erroExcecao:

        print(f'Erro de exceção: {erroExcecao}')
