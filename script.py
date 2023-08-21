""" 
Script para reorganizar arquivos xml dentro de uma pasta e suas subpastas.
"""
import os
import shutil

def reorganizar_arquivos(
    diretorio_origem="data", diretorio_destino="output", arquivos_por_pasta=1000):
    """
    Reorganiza arquivos de um diretório e suas subpastas em novas pastas no diretório de destino,
    com uma quantidade especificada de arquivos por pasta.

    Args:
        diretorio_origem (str): O diretório de origem dos arquivos XML.
        diretorio_destino (str): O diretório de destino para as novas pastas organizadas.
        arquivos_por_pasta (int): Quantidade de arquivos por pasta no diretório de destino.

    Returns:
        None
    """
    # Coletar todos os arquivos XML
    todos_arquivos = []
    for pasta in os.listdir(diretorio_origem):
        pasta_atual = os.path.join(diretorio_origem, pasta)
        for subpasta in os.listdir(pasta_atual):
            subpasta_atual = os.path.join(pasta_atual, subpasta)
            for arquivo in os.listdir(subpasta_atual):
                if arquivo.endswith('.xml'):
                    todos_arquivos.append(os.path.join(subpasta_atual, arquivo))

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
