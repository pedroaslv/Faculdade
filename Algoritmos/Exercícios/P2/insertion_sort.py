'''
Vantagens: Implementação muito simples. Muito eficiente em listas pequenas. Troca de posições in-place.
Desvantagens: Ineficiente em listas grandes.
'''

def insertion_sort(lista):
    n = len(lista) # Armazenar o tamanho da lista
    
    for i in range(1, n): # percorrer a lista, começando pelo segundo elemento (posição 1)
        chave = lista[i] # definir que a chave é o elemento que está na posição i
        
        j = i-1 # varíavel auxiliar j, estará uma posição atrás do elemento da posição i
        
        while j >= 0 and lista[j] > chave: # Enquanto j for maior que 0 e o elemento da posição J for maior que a chave
            lista[j + 1] = lista[j] # Trocamos o elemento na posição J para a direita
            j -=1 # Decrementamos J para continuar trocando de posição comparando com os elementos anteriores enquanto a condição do while for verdadeira
        lista[j + 1] = chave # Inserimos a chave na posição correta
    


lista_principal = [9, 4, 3, 8, 7, 0, 6, 5]


print(f'Lista antes da ordenação:\n{lista_principal}\n\nLista após o Insertion Sort:\n')

insertion_sort(lista_principal)

print(lista_principal)
