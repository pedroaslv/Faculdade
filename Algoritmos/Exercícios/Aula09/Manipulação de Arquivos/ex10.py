'''Escreva um programa que leia um arquivo grande, `grande.txt`, e divida seu conteúdo em
arquivos menores de no máximo 100 linhas cada. Nomeie os arquivos menores como
`parte_1.txt`, `parte_2.txt`, etc'''

with open('arquivos criados/grande.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    

parte = 1

for i in range(0, len(linhas), 99):
    with open(f'arquivos criados/parte_{parte}.txt', 'w') as arquivo:
        arquivo.writelines(linhas[i:i + 99])
    
    parte += 1