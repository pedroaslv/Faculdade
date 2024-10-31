'''- Escreva um programa que leia um arquivo `com_vazios.txt`, remova todas as linhas vazias e
salve o conteúdo em um novo arquivo chamado `sem_vazios.txt`.'''

with open('arquivos criados/com_vazios.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    linhas = conteudo.split('\n')
    linhas_preenchidas = [linha for linha in linhas if linha]

with open('arquivos criados/sem_vazios.txt', 'w') as arquivo:
    arquivo.writelines(linha + '\n' for linha in linhas_preenchidas)