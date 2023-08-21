# Organizador de Arquivos em Subpastas

[![GitHub](https://img.shields.io/badge/Visit-My%20Profile-0891B2?style=flat-square&logo=github)](https://github.com/Tgentil)

Este script foi desenvolvido para ajudar na reorganização de arquivos, independentemente de sua extensão, que estão distribuídos em diversas pastas e subpastas. Ele permite agrupar esses arquivos em novas pastas, com um número definido de arquivos por pasta.

## Como usar

1. Certifique-se de ter Python instalado em sua máquina.
2. Clone ou baixe este repositório.
3. Coloque seus arquivos na pasta "data" ou defina outro diretório de origem.
4. Execute o script.
5. Após a execução, você encontrará um arquivo "resumo_movimentacoes.txt" na raiz do projeto com um resumo das movimentações feitas.

## Funcionalidades

- Busca arquivos em todas as subpastas do diretório de origem.
- Cria pastas no diretório de destino com um número definido de arquivos em cada uma.
- Move os arquivos para as novas pastas criadas.
- Gera um resumo das movimentações em um arquivo de texto.

## Configurações

O script possui três argumentos que podem ser modificados:

- `diretorio_origem`: Diretório onde os arquivos estão localizados. Padrão é "data".
- `diretorio_destino`: Diretório onde as novas pastas serão criadas. Padrão é "output".
- `arquivos_por_pasta`: Quantidade de arquivos que cada nova pasta deve conter. Padrão é 1000.

## Exemplo de Uso

Para usar o script com as configurações padrão, simplesmente execute:

```
python script.py
```

Para especificar diferentes argumentos:

```
python script.py --diretorio_origem="meus_arquivos" --diretorio_destino="nova_organizacao" --arquivos_por_pasta=500
```

**Nota**: O exemplo acima de uso com argumentos específicos assume que você modifique o script para aceitar argumentos da linha de comando.

## Autor

* Thiago da Silveira Gentil
