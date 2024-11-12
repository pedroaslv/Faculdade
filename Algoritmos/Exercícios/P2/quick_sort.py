'''
Vantagens: Muito rápido na média dos casos. Requer pouca memória. Ordenação in-place.
Desvantagens: A escolha do pivot pode afetar o desempenho. Existem técnicas para melhorar a escolha.
'''

def partition(lista, inicio, fim):
    pivot = lista[fim]
    
    i = inicio - 1
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i+1], lista[fim] = lista[fim], lista[i+1]

    return i+1 #retorna a posição do pivo

def quick_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio < fim: # caso base para interromper a recursividade
        indice_pivot = partition(lista, inicio, fim)
        quick_sort(lista, inicio, indice_pivot-1)
        quick_sort(lista, indice_pivot+1, fim)


lista_principal = [9, 4, 3, 8, 7, 0, 6, 5]


print(f'Lista antes da ordenação:\n{lista_principal}\n\nLista após o Merge Sort:\n')

quick_sort(lista_principal)
print(lista_principal)

