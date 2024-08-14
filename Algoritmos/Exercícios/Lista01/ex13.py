#13. Soma dos Elementos de uma Lista 
#Crie uma lista de números e escreva um programa que some todos os elementos dessa lista.

import random

def soma(lst):
    soma = 0
    for num in lista:
        soma+=num
    return soma

lista = [random.randint(1,10) for num in range(10)]

    
print(f'A lista é: {lista} e sua soma vale: {soma(lista)}') 