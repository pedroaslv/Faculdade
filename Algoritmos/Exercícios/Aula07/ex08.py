'''Crie um dicionário que armazene a quantidade de produtos em estoque em uma loja.
Escreva uma função que verifique se um produto está em estoque e quantas unidades estão
disponíveis.'''

produtos = {
    'Camisa': 100,
    'Relógio': 0,
    'Bola': 50      
}

def disponibilidade(dicionario, produto):
    if produto in dicionario and dicionario[produto] > 0:
        return f'{produto} está disponível com {dicionario[produto]} de estoque.'
    
    else:
        return 'Produto indisponível.'

res = disponibilidade(produtos, 'Camisa')

print(res)