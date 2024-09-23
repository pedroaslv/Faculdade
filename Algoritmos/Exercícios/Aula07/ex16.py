#Escreva uma função de busca binária recursiva

def busca_binaria_recursiva(lista, alvo, ini=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if ini <= fim:
        mei = (ini + fim) // 2
    
        if lista[mei] == alvo:
            return mei

        if lista[mei] > alvo:
            return busca_binaria_recursiva(lista, alvo, ini, mei - 1)
        else:
            return busca_binaria_recursiva(lista, alvo, mei + 1, fim)
    
    return -1
