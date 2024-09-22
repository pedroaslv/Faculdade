'''Escreva um programa que receba 5 nomes de frutas do usuário e os armazene em uma lista.
Depois, peça ao usuário que informe uma fruta e verifique se ela está na lista.'''

frutas = []

for i in range(5):
    nova_fruta = input(f'Digite a fruta {i+1} da lista: ')
    frutas.append(nova_fruta)

fruta = input('Informe uma fruta para verificar se está na lista: ')

if fruta in frutas:
    print(f'{fruta} está na lista.')
else:
    print(f'{fruta} NÃO está na lista.')