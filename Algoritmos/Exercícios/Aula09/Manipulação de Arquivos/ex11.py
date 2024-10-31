'''- Escreva um programa que leia um arquivo `nomes.txt`, onde cada linha contém um nome.
 - Ordene os nomes em ordem alfabética e grave o resultado em um novo arquivo chamado
`nomes_ordenados.txt`.'''

pessoas = [
    'Otavio', 'Vanessa', 'Kleber', 'Igor', 'Natalia', 'Paula',
    'Eduardo', 'Paula', 'Thiago', 'Sofia', 'Larissa', 'Gabriel',
    'Bruno', 'Heloisa', 'Vanessa', 'Ana', 'David', 'Juliana']

with open('arquivos criados/nomes.txt', 'w') as arquivo:
    for pessoa in pessoas:
        arquivo.write(pessoa + '\n')

with open('arquivos criados/nomes.txt', 'r') as arquivo:
    nomes = [nome for nome in arquivo]
    nomes.sort()

with open('arquivos criados/nomes_ordenados.txt', 'w') as arquivo:
    arquivo.writelines(nomes)