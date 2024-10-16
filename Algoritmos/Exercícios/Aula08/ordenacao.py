import random
import time

def bubble_sort(lista):
    n = len(lista)
    
    for i in range(n-1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                     
    return lista
    
def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        menor_indice = i
        
        for j in range(i+1, n):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
       
    return lista


n = 100000 #100 mil elementos. Mais que isso demora muito.

lista_bubble = [random.randint(1, n) for x in range(n)]
lista_selection = lista_bubble.copy()

tempo_inicio_bubble = time.time()
bubble_sort(lista_bubble)
tempo_final_bubble = time.time() - tempo_inicio_bubble

tempo_inicio_selection = time.time()
selection_sort(lista_selection)
tempo_final_selection = time.time() - tempo_inicio_selection

print('COMPARATIVO DE TEMPO DE EXECUÇÃO:')
print('-'*50)
print(f'Elementos da Lista: {n}')
print(f'Bubble Sort: {tempo_final_bubble:.1f}s.')
print(f'Selection Sort: {tempo_final_selection:.1f}s.')

#caso fosse exibir a lista ordenada:
#print(lista_selection)