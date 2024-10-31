'''Crie um programa que peça ao usuário o nome de uma cor e mostre seu valor em RGB de acordo com um dicionário
pré-definido. O programa deve tratar exceções caso o nome da cor não exista
no dicionário.
cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': (0, 0, 255)}'''

cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': (0, 0, 255)}

try:
    cor = input('Informe a cor que deseja saber o padrão RGB: ')
    print(f'O padrão da cor {cor} é: {cores[cor]}')

except KeyError:
    print(f'A cor escolhida ({cor}) não consta na base de dados.')