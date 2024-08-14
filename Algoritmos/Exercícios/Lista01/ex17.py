#17. Calculando a Sequência de Fibonacci 
#Escreva um programa que gera os primeiros 10 números da sequência de Fibonacci.

def fibonacci(termos):
    a = 0
    b = 1    
    print(f'{a} | {b}', end = ' | ')
    for i in range(termos-2):
        c = a + b
        print(c, end = ' | ')
        a = b
        b = c

fibonacci(10)