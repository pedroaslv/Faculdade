'''Escreva uma função que receba um dicionário contendo nomes de produtos como chaves e
seus preços como valores. A função deve retornar o nome do produto mais caro.'''

dicio = {
    'Camisa': 100,
    'Bola': 505,
    'Boneco': 85,
    'Casaco': 325 
}

def produto_caro (dicionario):
    mais_caro = max(dicionario.values())
    
    for chave, valor in dicionario.items():
        if valor == mais_caro:
            return f'{chave}: {valor}'


res = produto_caro(dicio)

print(f'O produto mais caro é {res}')