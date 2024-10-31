'''Contar Linhas e Palavras
 - Escreva um programa que leia o conteúdo de um arquivo `texto.txt`.
 - Conte quantas linhas e palavras o arquivo possui e exiba esses valores no console.'''


with open(r'arquivos criados\texto.txt', 'w') as arquivo:
    arquivo.write('Python facilisis, justo eu iaculis volutpat, ')
    arquivo.write('dui sem orci, eget commodo odio mi in magna.\n')
    arquivo.write('Aenean elementum ex justo, sit amet varius eros suscipit id.')


with open(r'arquivos criados\texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    linhas = len(conteudo.split('\n'))
    palavras = len(conteudo.split())    
    print(f'O texto lido possui {linhas} linha(s) e {palavras} palavra(s).')