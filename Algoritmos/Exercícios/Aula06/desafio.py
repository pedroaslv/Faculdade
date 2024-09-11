"""Escreva um algoritmo recursivo que crie uma senha gerada de forma aleatória e que seja criptografada caractere por caractere usando uma cifra de César simples.
Aqui está um exemplo com uma criptografia simples usando a técnica de cifra de César. Esse exemplo adiciona um deslocamento de 3 posições no valor ASCII de cada caractere da senha gerada.
Senha original: A1b2C3d4.               
Senha criptografada: D4e5F6g7"""

import random
import string
numeros = string.digits
letras = string.ascii_letters
deslocamento = 3 

def gerar_senha(tamanho, indice=0):    
    if tamanho == 0:
        return "",""
    
    if indice % 2 == 0:
        indice_random = random.randint(0,len(letras)-1)
        indice_cesar = (indice_random + deslocamento) % len(letras)
        caractere_original = letras[indice_random]
        caractere_criptografado = letras[indice_cesar]
    
    else:
        indice_random = random.randint(0,len(numeros)-1)
        indice_cesar = (indice_random + deslocamento) % len(numeros)
        caractere_original = numeros[indice_random]
        caractere_criptografado = numeros[indice_cesar]
        
    original_resto, criptografada_resto = gerar_senha(tamanho - 1, indice + 1)
    
    senha_original = caractere_original + original_resto
    senha_criptografada = caractere_criptografado + criptografada_resto
        
    return senha_original, senha_criptografada   


resultado_original, resultado_criptografado = gerar_senha(8)
print(f'Senha Original: {resultado_original}\nSenha Criptografada: {resultado_criptografado}')