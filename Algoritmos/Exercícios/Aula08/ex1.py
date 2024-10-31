'''Escreva um programa que peça ao usuário
dois números e faça a divisão do primeiro pelo segundo. Se o usuário inserir
um valor inválido ou tentar dividir por zero, o programa deve exibir uma
mensagem de erro apropriada.'''

try:
    num1 = float(input('Informe o numerador: '))
    num2 = float(input('Informe o denominador: '))
    resultado = num1 / num2
    print(f'O resutado da divisão de {num1} por {num2} é {resultado}')

except ZeroDivisionError:
    print('Impossivel dividir por zero.')

except ValueError:
    print('O valor inserido é inválido.')

finally:
    print('Programa encerrado.')