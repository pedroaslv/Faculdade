#3. Verificar Par ou Ímpar 
#Peça ao usuário para digitar um número inteiro e informe se o número é par ou ímpar.
num = int(input('Digite um número inteiro: '))

if num % 2 == 0:
    print(f'O número digitado foi {num}, que é par.')
else:
    print(f'O número digitado foi {num}, que é ímpar.')