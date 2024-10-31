'''Escrever em um Arquivo de Texto
 - Crie um programa que peça ao usuário para digitar uma frase.
 - Escreva essa frase em um novo arquivo chamado `frase_usuario.txt`.'''


frase = input('Escreva uma frase: ')
with open(r'arquivos criados\frase_usuario.txt', 'w') as arquivo:
    input
    arquivo.write(frase)
