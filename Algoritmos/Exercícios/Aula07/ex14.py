'''Escreva uma função que receba um dicionário representando um estoque de produtos
(chave: nome do produto, valor: quantidade em estoque) e um produto vendido (nome do
produto e quantidade vendida). A função deve atualizar o estoque conforme a venda e
informar se a quantidade vendida excede o estoque disponível.
'''

estoque = {
    'Notebook': 2,
    'Monitor': 5,
    'Televisão': 1,
    'Teclado': 15
}

def venda_produto(dicionario, produto, qtd_vendida):
    dicionario[produto] -= qtd_vendida
    if dicionario[produto] < 0:
        print('A quantidade vendida excedeu o estoque do produto.')

    return f'Estoque atualizado: {dicionario }'


res = venda_produto(estoque, 'Notebook', 1)

print(res)