'''- Crie um programa que leia o conteúdo de um arquivo `texto.txt`.
 - Substitua todas as ocorrências de uma palavra (por exemplo, "Python") por outra (por
exemplo, "programação") e salve o conteúdo alterado em um novo arquivo chamado
`texto_modificado.txt`.'''

with open('arquivos criados/texto.txt', 'r') as arquivo:
    conteudo = arquivo.read().replace('Python','Pitão')


with open('arquivos criados/texto.modificado.txt', 'w') as arquivo:
    arquivo.write(conteudo)