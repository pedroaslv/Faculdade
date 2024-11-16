'''
Vantagens: Eficiente em dados uniformes, com intervalos definidos e conhecidos. Ex( 0.1 a 0.9) 

Desvantagens: Demanda tempo extra para alocar os itens nos buckets. Dados com número inteiros longos.
'''


def insertion_sort(bucket): #criar um insertion sort é necessário para o bucket sort
    for i in range(1, len(bucket)):
        chave = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > chave:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = chave

def bucket_sort(lista):

    n = len(lista)
    valor_maximo = max(lista)
    valor_minimo = min(lista)
    intervalo = valor_maximo - valor_minimo + 1
    buckets = [[] for _ in range(n)]
    
    for num in lista: #coloca cada elemento em diferentes "baldes", o critério para isso é o arredondamento para um número inteiro do número após sua multiplicação pela quantidade de índices que a lista tem.
        bucket_index = int((num - valor_minimo) / (intervalo) * (n))
        buckets[bucket_index].append(num)
    

    for bucket in buckets: #organiza cada "balde" individualmente usando o insertion sort
        insertion_sort(bucket)
    
    indice = 0
    for bucket in buckets: #reorganiza os elementos de volta na lista original se baseando nos "baldes" agora organizados
        for num in bucket:
            lista[indice] = num
            indice += 1



numeros = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]

bucket_sort(numeros)
print(numeros)