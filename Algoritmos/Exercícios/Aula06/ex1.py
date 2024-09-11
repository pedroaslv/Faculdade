#Implemente uma função recursiva que calcule a potência de um número (base^expoente).

def potenciacao(n, p):
    if p == 0:
        return 1
    
    return n * (potenciacao(n,p-1))

resultado = potenciacao(5,3)
print(resultado)
