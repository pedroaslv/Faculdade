'''Crie uma lista de listas onde cada sublista deve conter três elementos: o nome de uma
pessoa, sua idade e sua cidade. Imprima todas as informações no formato: "Nome: [Nome],
Idade: [Idade], Cidade: [Cidade]"'''

listas = [
    ['Pedro', 32, 'Araruama'],
    ['Mariana', 26, 'Seropédica'],
    ['Silvia', 57, 'Saquarema']   
]

for sublista in listas:
    print(f'Nome: {sublista[0]}, Idade: {sublista[1]}, Cidade: {sublista[2]}')