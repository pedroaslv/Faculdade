#9. Verificar Número Primo 
#Peça ao usuário para digitar um número e verifique se ele é primo.

num = int(input('Digite um número: '))

c = 0
for i in range(1,num+1):
    if num%i == 0:
        c+=1

if c > 2:
    print(f'Você digitou o número {num}, que NÃO é um número primo.')
else:
    print(f'Você digitou o número {num}, que É um número primo.')
    