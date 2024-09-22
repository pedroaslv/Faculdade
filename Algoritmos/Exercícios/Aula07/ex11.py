'''Escreva uma função que receba uma lista de números e retorne a soma de todos os
números pares dessa lista.'''
import random
lista_num = [random.randint(1,15) for x in range(10)]

def soma_pares(lista):
    soma = 0
    for num in lista_num:
        if num % 2 == 0:
            soma+=num
    return soma

res = soma_pares(lista_num)

print(f'A lista é: {lista_num}')
print(f'A soma dos pares é: {res}')