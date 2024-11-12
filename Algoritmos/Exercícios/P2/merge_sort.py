'''
DIVIDIR PARA CONQUISTAR

Divide a lista desordenada em duas sublistas, metade da original
Continua dividindo as sublistas enquanto cada parte tiver mais de um elemento
Mescla 2 sublistas sempre colocando o menor valor entre elas primeiro
Continua mesclando até que não tenha mais sublista nenhuma.

Vantagens: Ótima opção para grandes listas, pois é consistente em todos os casos. Funciona bem com números e strings.
Desvantagens: Requer espaço adicional de memória para armazenar as sublistas durante a mesclagem. Não é in-place.
'''

def merge_sort(lista):
    if len(lista) <= 1: # Caso base. Se a lista tiver 1 ou 0 elementos, já está ordenada.
        return lista
    
    mid = len(lista) // 2 # Encontra o indíce do meio
    metade_esquerda = lista[:mid] # Divide a lista em esquerda
    metade_direita = lista[mid:] # e direita
    
    esquerda_ordenada = merge_sort(metade_esquerda) # Ordena recursivamente a metade da esquerda
    direita_ordenada = merge_sort(metade_direita) # Ordena recursivamente a metade da direita
    
    return merge(esquerda_ordenada, direita_ordenada) # Mescla as duas metades ordenadas.

def merge(esquerda, direita):
    resultado = []
    
    i, j = 0, 0 # I índice da lista esquerda. J índice da lista direita.
    
    while i < len(esquerda) and j < len(direita): # Enquanto houver elemento nas listas da esquerda e da direita
        if esquerda[i] < direita[j]: # Se o elemento da esquerda for menor que o da direita
            resultado.append(esquerda[i]) # Adiciona o elemento da esquerda na lista auxiliar
            i += 1 # Incrementa o índice da esquerda
        else:
            resultado.append(direita[j]) # Caso contrário, adiciona o elemento da direita lista auxiliar
            j += 1 # Incrementa o índice da direita
            
    # Quando uma das listas for totalmente percorrida:
    resultado.extend(esquerda[i:]) # Adiciona os elementos restantes da esquerda
    resultado.extend(direita[j:]) # Adiciona os elementos restantes da direita
    
    return resultado # retorna a lista ordenada

lista_principal = [8, 6, 1, 5, 4, 3, 7, 2]
lista_final = merge_sort(lista_principal)

print(f'Lista antes da ordenação:\n{lista_principal}\n\nLista após o Merge Sort:\n{lista_final}')
