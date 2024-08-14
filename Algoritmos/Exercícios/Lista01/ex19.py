#19. Verificar Palíndromo 
#Peça ao usuário para digitar uma palavra e verifique se ela é um palíndromo (lê-se da mesma forma de trás para frente).

palavra = input('Digite uma palavra: ').upper()
palavraInv = ''
for letra in palavra:
    palavraInv = letra + palavraInv

if palavra == palavraInv:
    print(f'{palavra}>-<{palavraInv} É um palíndromo.')
else:
    print(f'{palavra}>-<{palavraInv} NÃO é um palíndromo.')