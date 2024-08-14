#15. Números Pares em uma Lista 
#Dada uma lista de números, crie um programa que exiba apenas os números pares.

import random

lista = [random.randint(1,10) for num in range(10)]

print(f'A lista é {lista} e os pares são: ', end = '')
for i, num in enumerate(lista):
    if num % 2 == 0:
        print(num, end = ' | ')
