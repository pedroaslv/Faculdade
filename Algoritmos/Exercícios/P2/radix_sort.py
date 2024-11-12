'''
Vantagens: Ideal para dados com intervalos pequenos.

Desvantagens: Não funciona bem com com todos tipos de dados, como inteiros negativo.

'''

def radix_sort(lista):
    listas_radix = [[], [], [], [], [], [], [], [], [], []]
    maior = max(lista)
    exp = 1

    while maior // exp > 0: # vai fazer as operações até que expoente atinja o mesmo número de casas que o maior número da lista

        while len(lista) > 0: 
            temporario = lista.pop()
            indice_radix = (temporario // exp) % 10 
            listas_radix[indice_radix].append(temporario)

        for bucket in listas_radix:
            while len(bucket) > 0:
                temporario = bucket.pop()
                lista.append(temporario)
                
        exp *= 10
    
    return lista

lista_principal = [533, 278, 442, 729, 707]

print(f'Lista antes da ordenação:\n{lista_principal}\n\nLista após o Radix Sort:')
radix_sort(lista_principal)

print(lista_principal)