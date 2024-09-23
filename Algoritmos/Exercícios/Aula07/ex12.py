'''Escreva uma função que receba um dicionário contendo nomes de produtos como chaves e
seus preços como valores. A função deve retornar o nome do produto mais caro.'''

dicio = {
    'Camisa': 100,
    'Bola': 55,
    'Boneco': 85,
    'Casaco': 325 
}

def produto_caro (dicionario):
    mais_caro = 0
    for produto, valor in dicionario.items():
        if valor >= mais_caro:
            mais_caro = valor
        
    return produto

res = produto_caro(dicio)

print(f'O produto mais caro é {res}')