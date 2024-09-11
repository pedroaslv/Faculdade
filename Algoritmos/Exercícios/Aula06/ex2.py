#Crie uma função recursiva para calcular o n-ésimo termo da sequência de Fibonacci.Lembre-se de que a sequência começa com 0 e 1.

def fibonacci(n):
    if n < 0:
        return 'Não há termo negativo em Sequência de Fibonacci.'
    
    if n < 2:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

resultado = fibonacci(12)
print(resultado)
