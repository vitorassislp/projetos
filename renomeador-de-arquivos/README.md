Renomeador de Arquivos

Este projeto é um script em Python que renomeia arquivos dentro de uma pasta escolhida pelo usuário. O objetivo é facilitar a organização de arquivos que seguem um mesmo padrão, como imagens, documentos ou qualquer outro tipo de extensão.

Como funciona

1. O programa abre uma janela para que o usuário selecione uma pasta.
2. Depois, o usuário informa qual é a extensão dos arquivos que deseja renomear, por exemplo: ".png" ou ".pdf".
3. Em seguida, o usuário define o nome base que será usado nos novos arquivos, por exemplo: "Imagem".
4. O programa percorre todos os arquivos da pasta e renomeia apenas aqueles que possuem a extensão informada.
5. Os arquivos são renomeados seguindo o padrão NomeBase_1.extensao, NomeBase_2.extensao e assim por diante.

Requisitos

Python 3 instalado.  
A biblioteca Tkinter já vem instalada junto com o Python na maioria das versões.

Como executar

1. Salve o arquivo do script em algum local do seu computador.
2. Abra o terminal e navegue até a pasta onde o arquivo está.
3. Execute o comando:

python nome_do_arquivo.py

4. A janela para escolher a pasta irá aparecer e o processo começará.

Estrutura básica do código

O script utiliza as bibliotecas os e tkinter.  
Ele segue uma função principal que cuida da lógica do programa e só é executada caso o arquivo seja aberto diretamente.

Objetivo do projeto

Este projeto serve como prática de automação com Python. Ele ajuda quem está começando a aprender sobre manipulação de arquivos, uso do Tkinter e organização de código.

Licença

Você pode usar, modificar ou adaptar este código como quiser.