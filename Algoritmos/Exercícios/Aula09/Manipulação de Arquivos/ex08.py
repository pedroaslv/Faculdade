'''Combinar Vários Arquivos
 - Crie um programa que leia o conteúdo de três arquivos (`parte1.txt`, `parte2.txt` e
`parte3.txt`).
 - Combine o conteúdo dos três arquivos em um novo arquivo chamado `texto_completo.txt`.
'''

with open('arquivos criados/parte1.txt', 'w') as arquivo:
    arquivo.write('Esse é o texto inicial, ')

with open('arquivos criados/parte2.txt', 'w') as arquivo:
    arquivo.write('esse é o texto do meio, ')

with open('arquivos criados/parte3.txt', 'w') as arquivo:
    arquivo.write('esse é o texto final.')    

with open('arquivos criados/parte1.txt', 'r') as arquivo:
    conteudo = arquivo.read()

with open('arquivos criados/parte2.txt', 'r') as arquivo:
    conteudo += arquivo.read()

with open('arquivos criados/parte3.txt', 'r') as arquivo:
    conteudo += arquivo.read()

with open('arquivos criados/texto_completo.txt', 'w') as arquivo:
    arquivo.write(conteudo)
