"""
Renomeador Automático de Arquivos

Este script permite renomear todos os arquivos de uma pasta,
aplicando um nome base e numeração sequencial com zeros à esquerda.

Tecnologias:
- Python
- Tkinter (para seleção da pasta)
- os (manipulação de arquivos e diretórios)

Autor: Vitor Assis Leppaus
GitHub: https://github.com/vitorassislp
"""

from tkinter import filedialog, Tk
import os


def renomear_arquivos(caminho, extensao, nome_base):

    """
    Usado para renomear arquivos dentro de um diretório baseado em uma extensão específica.

    Args:
        caminho (str): Caminho da pasta escolhida.
        extensao (str): Extensão dos arquivos (ex: ".png", ".pdf").
        nome_base (str): Nome base para o novo arquivo (ex: "Imagem").

    Returns:
        int: Quantidade de arquivos renomeados.
    """

    contador = 1
    arquivos = os.listdir(caminho)
    alterados = 0

    for arquivo in arquivos:

        caminho_antigo = os.path.join(caminho, arquivo)

        # ignora diretorios
        if not os.path.isfile(caminho_antigo):
            continue

        # verifica extensão correta
        if not arquivo.lower().endswith(extensao.lower()):
            continue

        # monta nome com zeros à esquerda -> 001, 002, 003...
        novo_nome = f"{nome_base}_{contador:03d}{extensao}"
        caminho_novo = os.path.join(caminho, novo_nome)

        try:
            os.rename(caminho_antigo, caminho_novo)
            print(f"Renomeado: {arquivo}  →  {novo_nome}")
            contador += 1
            alterados += 1

        except Exception as e:
            print(f"Erro ao renomear {arquivo}: {e}")

    return alterados


def main():
    
    """Função principal do programa."""

    root = Tk()
    root.withdraw()  # oculta janela principal Tkinter

    print("\n--- RENOMEADOR DE ARQUIVOS ---\n")

    caminho = filedialog.askdirectory(title="Selecione uma pasta")

    if not caminho:
        print("Nenhuma pasta selecionada. Encerrando o programa.")
        return

    extensao = input('Digite a extensão (ex: ".png"): ').strip()
    nome_base = input('Digite o nome base (ex: "Imagem"): ').strip()

    if not extensao.startswith("."):
        print("Extensão inválida! Ela deve começar com ponto. Exemplo: .png")
        return

    quantidade = renomear_arquivos(caminho, extensao, nome_base)

    print(f"\nProcesso concluído. {quantidade} arquivo(s) renomeado(s).")
    root.destroy()


if __name__ == "__main__":
    main()
