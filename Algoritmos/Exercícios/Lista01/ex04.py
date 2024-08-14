# 4. Calculadora Simples 
#Crie um programa que peça dois números e a operação desejada (+, -, *, /) e exiba o resultado.
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operacao = input('Digite a operação desejada (+, -, *, /): ')

if operacao == '+':
    resultado = num1 + num2
    
elif operacao == '-':
    resultado = num1 - num2

elif operacao == '*':
    resultado = num1 * num2

elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print('Não é possível dividir por 0.')

else:
    print('Operação inválida.')

print(f'{num1} {operacao} {num2} = {resultado}')

