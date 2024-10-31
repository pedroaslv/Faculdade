'''Ler um Arquivo de Texto
 - Crie um arquivo de texto chamado `mensagem.txt` com algumas linhas de texto.
 - Escreva um programa que leia todo o conteúdo desse arquivo e o exiba no console.'''

with open(r'arquivos criados\mensagem.txt', 'w') as arquivo:
    arquivo.write('O Flamengo foi campeão de 2019 com um grande elenco.\n')
    arquivo.write('Liderado pelo grande Jorge Jesus.')

with open(r'arquivos criados\mensagem.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)