from typing import Dict
import os
import csv

class Dados:
    """Classe abstrata para lidar com leitura e escrita de arquivos"""

    @staticmethod
    def ler_dados(nome_arquivo : str, separador: str = ",") -> Dict:
        if not os.path.isfile(nome_arquivo):
            print (f"Arquivo '{nome_arquivo}' Não existe sob {os.getcwd()}. Retornando dicionário com parâmetros padrão")
        else:
            with open(nome_arquivo, 'r') as arq:
                dados = {}
                linhas = csv.reader(arq, delimiter=separador)
                for linha in linhas:
                    # Ignorar linha de cabeçalho/comentário
                    if linha[0].startswith('#'):
                        continue
                    # Atribui o primeiro campo como chave e o segundo como valor
                    dados[linha[0].strip()] = linha[1].strip()
            return dados
