#11. Tabuada 
#Peça ao usuário para digitar um número e imprima a tabuada desse número de 1 a 10.

num = int(input('Digite o número que deseja saber sua tabuada até 10: '))

print('~~TABUADA~~')
for n in range(1,11):
    print(f'{num} x {n} = {num*n}')
print('~'*11)