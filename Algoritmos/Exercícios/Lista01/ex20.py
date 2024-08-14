#20. Jogo de Adivinhação 
#Crie um programa onde o computador escolhe um número aleatório entre 1 e 100 e o usuário deve tentar adivinhar o número. O programa deve dar dicas se o número escolhido é maior ou menor que a tentativa do usuário.

import random

numero = random.randint(1,100)

palpite = int(input('Tente adivinhar o número sorteado (1 a 100): '))
c = 1
while palpite != numero:
    if palpite > numero:
        print(f'O número que sorteado é MENOR que o seu palpite({palpite}).')
    else:
        print(f'O número que sorteado é MAIOR que o seu palpite({palpite}).')
    palpite = int(input('Tente adivinhar o número sorteado (1 a 100): '))
    c+=1

print(f'Acertou, em {c} tentativas! O número sorteado foi: {numero}.')