'''Escreva um programa que solicite um número ao
usuário. Se o número for maior que 10, exiba uma mensagem dizendo que o
número é válido. Utilize o bloco else para imprimir que o programa foi
executado com sucesso, e o bloco finally para imprimir "Programa
encerrado".'''

try:
    num = int(input('Informe um número: '))

    if num > 10:
        print('Número válido.')
    
    else:
        print('O programa foi executado com sucesso.')

except ValueError:
    print('O valor informado não é válido.')

finally:
    print('Programa encerrado.')