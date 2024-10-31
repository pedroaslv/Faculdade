'''Copiar Conteúdo de um Arquivo
 - Escreva um programa que leia o conteúdo de um arquivo chamado `origem.txt` e o copie
para um novo arquivo chamado `copia.txt`.'''

with open('arquivos criados/origem.txt', 'w') as arquivo:
    arquivo.write('Este é um conteúdo genérico para copiar.')

with open('arquivos criados/origem.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    
with open('arquivos criados/copia.txt', 'w') as arquivo:
    arquivo.write(conteudo)
