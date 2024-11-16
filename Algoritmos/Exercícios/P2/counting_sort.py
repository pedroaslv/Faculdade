'''
É um algoritmo que ordena por contagem de ocorrências.

Vantagens:
Simples de implementar
Quando os elementos da lista são inteiros pequenos e positivos é uma excelente opção.
Quando a lista auxiliar é menor do que a lista principal, torna-se efeciente, economizando.

Desvantagens:
Só funciona em lista de número inteiros e positivos.
Se o número de valores distintos possíveis (k) for maior que o número de valores a serem ordenados (n)
A lista de contagem será maior que a original e o algoritmo será ineficaz.


'''

def counting_sort(lista):
    maior = max(lista) # Encontra o maior valor na lista para determinar o tamanho do lista de contagem

    
    contagem = [0] * (maior + 1) # Cria uma lista de contagem com zeros, com tamanho suficiente para armazenar a contagem de cada valor até o maior valor
    
    while len(lista) > 0: # Enquanto a lista principal tiver elementos, conta a ocorrência de cada número
        num = lista.pop(0) # Atribui o primeiro elemento da lista a variável {num} e o remove
        contagem[num] += 1 # Incrementa a contagem para o valor {num} na lista de contagem.
    
    for i in range(len(contagem)): # Refaz a lista principal com base nas contagens 
        while contagem[i] > 0: # Adiciona o número {i} na lista final, o número de vezes que ele foi contado
            lista.append(i)
            contagem[i] -=1 # Decrementa o número {i} da lista contagem toda vez q ele é adiciona à lista final

    return lista
    
lista_principal = [7, 5, 6, 1, 5, 2, 6, 6, 5, 2, 5]


print(f'Lista antes da ordenação:\n{lista_principal}\n\nLista após o Counting Sort:')
counting_sort(lista_principal)

print(lista_principal)