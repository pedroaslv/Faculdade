'''Escreva uma função que recebe uma lista de dicionários, onde cada dicionário representa
um estudante com seu nome e uma lista de notas. A função deve calcular a média de cada
estudante e retornar um novo dicionário com os nomes dos estudantes como chaves e suas
médias como valores.'''

estudantes = [
    {'Pedro': [7, 8]},
    {'Douglas': [10, 9]},
    {'Raphael': [8, 8]},
    {'Erica': [9, 7]}    
    ]


def media(lista):
    dicio = {}
    
    for aluno in lista:
        soma = 0
        for chave, valor in aluno.items():
            for nota in valor:
                soma+= nota
        media = soma / len(valor)
        dicio[chave] = media
    return dicio

print(media(estudantes))