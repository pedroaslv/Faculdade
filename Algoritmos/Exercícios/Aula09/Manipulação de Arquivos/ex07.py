'''Escreva um programa que liste todos os arquivos e diretórios de um determinado diretório
(dica: use `os.listdir()`).
 - Peça ao usuário para informar o caminho do diretório desejado.'''

import os

caminho = input('Informe o diretório que deseja listar todos os arquivos: ')

lista_dir = os.listdir(caminho)

print(lista_dir)