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

    # Certifique-se de que o diretório de destino exista
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    # Mova os arquivos para as novas pastas
    for i, arquivo in enumerate(todos_arquivos):
        pasta_atual = os.path.join(diretorio_destino, f'pasta_{i // arquivos_por_pasta}')
        if not os.path.exists(pasta_atual):
            os.makedirs(pasta_atual)
        shutil.move(arquivo, os.path.join(pasta_atual, os.path.basename(arquivo)))

reorganizar_arquivos()
