'''
Vantagens: Consome pouco espaço extra. Bom para contextos de memória limitada.

Desvantagens: Instabilidade, não preserva ordem de elementos iguais.

'''


def heapify(lista, n, i): #função que irá transformar a lista em uma árvore binária
    
    maior = i #o indice 0 representa o valor mais alto na hierarquia

    esquerda = 2 * i + 1 #vai definir os numeros que vão pra esquerda

    direita = 2 * i + 2 #vai definir os numeros que vão pra direita

    if esquerda < n and lista[esquerda] > lista[maior]: #if caso o filho da esquerda for maior que o valor do índice 0
        maior = esquerda

    if direita < n and lista[direita] > lista[maior]: #faz o mesmo que o da esquerda, mas com a direita, agora
        maior = direita
    
    if maior != i: #se o índice não for o maior valor...
        lista[i], lista[maior] = lista[maior], lista[i] #troca o índice pelo maior valor

        heapify(lista, n, maior) #vai executar essa função recursivamente até que o índice seja o maior

def heap_sort(lista):

    n = len(lista)

    for i in range(n // 2 - 1, -1, -1): #primeiro, começa do último nó não-folha e então aplica a função heapify, que vai ser aplicada denovo recursivamente até que a lista ou array se torne um max-heap (quando todos os pais sao maiores que seus filhos)
        heapify(lista, n, i)
    
    for i in range(n - 1, 0, -1): #um por um, reduz um elemento da heap

        lista[0], lista[i] = lista[i], lista[0] #move o índice 0 para o final

        heapify(lista, i, 0) #chama a função para aplicar um max-heap novamente no heap reduzido
    
lista = [9, 4, 3, 8, 10, 2, 5]

heap_sort(lista)
print(lista)