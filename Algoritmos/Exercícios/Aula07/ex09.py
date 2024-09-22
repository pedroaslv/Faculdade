'''Crie duas listas: uma com nomes de países e outra com suas respectivas capitais. Converta
essas duas listas em um dicionário, onde o país é a chave e a capital é o valor.'''

paises = ["França", "Japão", "Argentina", "Alemanha", "Itália","China"]
capitais = ["Paris", "Tóquio", "Buenos Aires", "Berlim", "Roma", "Pequim"]

# com métodos nativos:
dicio = dict(zip(paises, capitais))

# sem métodos nativos:

for i in range(len(paises)):
    dicio.update({paises[i]:capitais[i]})

print(dicio)