Sistema de controle de alunos em Python.

Este projeto foi desenvolvido em Python com o objetivo de gerenciar alunos de uma turma, permitindo cadastrar estudantes, calcular médias e gerar listagens de aprovados e reprovados.

O sistema é totalmente executado no terminal, por meio de um menu interativo.

O sistema permite:

Cadastrar alunos com:

- Nome
- Nota do Bimestre 1
- Nota do Bimestre 2
- Média automática

Com isso, é possível:

- Listar todos os alunos cadastrados
- Listar apenas os alunos aprovados
- Listar apenas os alunos reprovados
- Encerrar o programa pelo menu

O projeto está dividido em dois arquivos principais:

main.py

* Contém o menu principal
* Controla o fluxo do programa
* Chama as funções do arquivo `alunos.py`
* Armazena a lista `turma`

alunos.py

Contém todas as funções responsáveis por:

  - Ler o nome do aluno
  - Ler as notas dos bimestres
  - Listar alunos
  - Filtrar aprovados
  - Filtrar reprovados

Exemplo do menu:

Menu Principal
(1) Cadastrar aluno
(2) Mostrar listagem de alunos
(3) Mostrar aprovados
(4) Mostrar reprovados
(0) Finalizar programa

Regras:

A média do aluno é calculada assim:

média = (notaB1 + notaB2) / 2

Por padrão no projeto:

Aprovado: média maior ou igual a 6
Reprovado: média menor que 6

Como executar:

1. Certifique-se de ter o Python instalado
2. Coloque os arquivos `main.py` e `alunos.py` na mesma pasta
3. No terminal, acesse a pasta do projeto
4. Execute o comando:

python main.py

ou, dependendo do sistema:

python3 main.py

Requisitos para rodar:

- Python 3.x
- Terminal (Prompt de Comando, PowerShell ou Terminal do Linux/Mac)
- Nenhuma biblioteca externa é necessária

Autor: Vitor Assis Leppaus