#Escreva uma função recursiva que verifique se uma string é um palíndromo.

def palindromo(texto):
    if len(texto) == 1:
        return True
    
    if texto[0].upper() != texto[-1].upper():
        return False
    
    return palindromo(texto[1:-1])

print(palindromo('Reinier'))