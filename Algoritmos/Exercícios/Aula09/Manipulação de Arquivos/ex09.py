'''- Suponha que você tenha um arquivo chamado `pessoas.txt` com dados no seguinte formato:
 Nome: Ana, Idade: 30
 Nome: Bruno, Idade: 25
 Nome: Carla, Idade: 35

 - Escreva um programa que leia o arquivo e exiba apenas os nomes das pessoas.'''
 
with open('arquivos criados/pessoas.txt', 'w') as arquivo:
    arquivo.write('Nome: Ana, Idade: 30\n')
    arquivo.write('Nome: Bruno, Idade: 25\n')
    arquivo.write('Nome: Carla, Idade: 35')

with open('arquivos criados/pessoas.txt', 'r') as arquivo:
    
    for linha in arquivo:
        nome = linha.split()[1].strip(',')
        print(nome)