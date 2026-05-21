import json
from aula144_a import CAMINHO_DO_ARQUIVO, Pessoa, fazer_dump

# fazer_dump()

with open(CAMINHO_DO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    
