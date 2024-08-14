# 8. Contagem de Números Ímpares 
#Escreva um programa que conta e imprime todos os números ímpares entre 1 e 100.

c = 0
for num in range(1,101):
    if num%2 != 0:
        print(num, end = ' | ')
        c+=1

print(f'\nForam contados {c} números ímpares.')