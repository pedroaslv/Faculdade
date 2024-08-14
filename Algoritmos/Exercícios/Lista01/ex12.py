#12. Contar Vogais em uma String 
#Escreva um programa que conte o número de vogais em uma string fornecida pelo usuário.

palavra = input('Escreva uma frase: ')
c = 0
for letra in palavra:
    if letra in 'aeiou':
        c+=1

print(f'A frase digitada possui {c} vogais.')