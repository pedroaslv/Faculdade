'''Crie uma lista de 10 elementos numéricos e escreva uma função que calcule a média dos números presentes na lista.'''
import random
lista = [random.randint(1,30) for num in range(10)]

def media(lista):
    soma = 0
    for num in lista:
        soma += num
    
    med = soma / len(lista)
    
    return med

resultado = media(lista)

print(f'A lista é {lista} e sua média é {resultado}.')