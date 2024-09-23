'''Crie uma função que recebe uma lista e um número opcional. Se o número for fornecido, a
função deve retornar a lista multiplicada por esse número. Se não for fornecido, a função deve
retornar a lista original.
'''
lista = [2, 4, 3, 10, 7]

def multiplcar(lista, numero = None):
    if numero != None:
       for i, num in enumerate(lista):
            lista[i] = num * numero
    
    return lista

res = multiplcar(lista, 3)

print(res)