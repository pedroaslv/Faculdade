'''Adicionar Conteúdo a um Arquivo
 - Escreva um programa que peça ao usuário para digitar uma frase.
 - Adicione essa frase ao final de um arquivo existente chamado `anotacoes.txt`'''

with open('arquivos criados/anotacoes.txt', 'w') as arquivo:
    arquivo.write('Este é o conteúdo que já estava no arquivo.\n')

frase = input('Escreva uma frase: ')

with open('arquivos criados/anotacoes.txt', 'a') as arquivo:
    arquivo.write(frase)