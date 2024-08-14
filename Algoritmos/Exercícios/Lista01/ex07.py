#7. Fatorial de um Número 
#Peça ao usuário para digitar um número e calcule o fatorial desse número.

num = fatorial = int(input('Digite o número inteiro que deseja saber o Fatorial: '))

print(f'O fatorial é {num} x ', end = '')
for i in range(num-1, 0, -1):
    fatorial*=i
    if i > 1:
        print(i, end = ' x ')
    else:
        print(i, end = f' = {fatorial}')