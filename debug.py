""" 
Script para reorganizar arquivos dentro de uma pasta e suas subpastas.
"""
import os
import shutil
import sys

# Define o enconding
sys.stdout.reconfigure(encoding='utf-8')

def coletar_arquivos(diretorio):
    """Coleta recursivamente todos os arquivos em um diretório e suas subpastas."""
    arquivos = []
    for item in os.listdir(diretorio):
        caminho_item = os.path.join(diretorio, item)
        if os.path.isfile(caminho_item):
            arquivos.append(caminho_item)
        elif os.path.isdir(caminho_item):
            arquivos.extend(coletar_arquivos(caminho_item))
    return arquivos

def reorganizar_arquivos(
    diretorio_origem="data", diretorio_destino="output", arquivos_por_pasta=1000):
    """
    Reorganiza arquivos de um diretório e suas subpastas em novas pastas no diretório de destino,
    com uma quantidade especificada de arquivos por pasta.

    Args:
        diretorio_origem (str): O diretório de origem dos arquivos.
        diretorio_destino (str): O diretório de destino para as novas pastas organizadas.
        arquivos_por_pasta (int): Quantidade de arquivos por pasta no diretório de destino.

    Returns:
        None
    """
    # Coletar todos os arquivos
    todos_arquivos = coletar_arquivos(diretorio_origem)
    print(f"Total de arquivos coletados: {len(todos_arquivos)}")

    # Rastrear movimentações
    movimentacoes_origem = {}
    movimentacoes_destino = {}

    # Certifique-se de que o diretório de destino exista
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    # Mova os arquivos para as novas pastas
    for i, arquivo in enumerate(todos_arquivos):
        pasta_origem = os.path.dirname(arquivo)
        pasta_atual_destino = os.path.join(diretorio_destino, f'pasta_{i // arquivos_por_pasta}')

        # Atualizar rastreamento
        movimentacoes_origem[pasta_origem] = movimentacoes_origem.get(pasta_origem, 0) + 1
        movimentacoes_destino[pasta_atual_destino] = movimentacoes_destino.get(pasta_atual_destino, 0) + 1

        # Mover arquivos
        if not os.path.exists(pasta_atual_destino):
            os.makedirs(pasta_atual_destino)
        print(f"Movendo {arquivo} para {pasta_atual_destino}")
        shutil.move(arquivo, os.path.join(pasta_atual_destino, os.path.basename(arquivo)))

    # Gravar resultados em um arquivo txt
    with open("resumo_movimentacoes.txt", "w", encoding="utf-8") as relatorio:
        relatorio.write("Resumo das Movimentações:\n\n")
        relatorio.write("Arquivos movidos de cada pasta origem:\n")
        for pasta, qtd in movimentacoes_origem.items():
            relatorio.write(f"{pasta}: {qtd} arquivos\n")

        relatorio.write("\nArquivos em cada pasta de destino:\n")
        for pasta, qtd in movimentacoes_destino.items():
            relatorio.write(f"{pasta}: {qtd} arquivos\n")

    print("Resumo das movimentações gravado em resumo_movimentacoes.txt")

reorganizar_arquivos()
