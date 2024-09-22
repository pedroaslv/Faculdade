'''Crie um dicionário que armazene os dias da semana como chaves e o número de horas
trabalhadas em cada dia como valores. Solicite ao usuário a entrada dessas horas e depois
calcule o total de horas trabalhadas na semana.'''

semana = {}

dias_da_semana = ('seg', 'ter', 'qua', 'qui', 'sex')

for dia in dias_da_semana:
    horas = int(input(f'Informe as horas trabalhadas na {dia}: '))
    semana.update({dia:horas})

horas = 0
for c, v in semana.items():
    print(f'{c}: {v}h')
    horas += v
print(f'Total de horas trabalhadas: {horas}h.')
