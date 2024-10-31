''' - Crie um programa que leia o conteúdo de um arquivo `secreto.txt`, "criptografe" o
conteúdo substituindo cada caractere por outro (por exemplo, substitua cada letra por sua letra
seguinte no alfabeto), e salve o conteúdo criptografado em um arquivo `criptografado.txt`.
 - Em seguida, escreva um programa para ler o `criptografado.txt` e "descriptografar" o
conteúdo para exibir o texto original.'''
import string
maiusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase   

def criptografar_texto(texto):
    resultado = ''
    
    for letra in texto:
        if letra in maiusculas:
            novo_indice = (maiusculas.index(letra) + 1) % len(maiusculas)
            resultado += maiusculas[novo_indice]
        
        elif letra in minusculas:
            novo_indice = (minusculas.index(letra) + 1) % len(minusculas)
            resultado += minusculas[novo_indice]    
        else:
            resultado += letra
        
    return resultado

def descriptografar_texto(texto):
    resultado = ''
    
    for letra in texto:
        if letra in maiusculas:
            novo_indice = (maiusculas.index(letra) - 1) % len(maiusculas)
            resultado += maiusculas[novo_indice]
        
        elif letra in minusculas:
            novo_indice = (minusculas.index(letra) - 1) % len(minusculas)
            resultado += minusculas[novo_indice]    
        else:
            resultado += letra
        
    return resultado

def criptografar_arquivo(arquivo_original, arquivo_criptografado):
    with open(arquivo_original, 'r') as arquivo:
        conteudo = arquivo.read()
    
    with open(arquivo_criptografado, 'w') as arquivo:
        novo_conteudo = criptografar_texto(conteudo)
        arquivo.write(novo_conteudo)

def descriptografar_arquivo(arquivo_criptografado):
    with open(arquivo_criptografado, 'r') as arquivo:
        conteudo = arquivo.read()
        novo_conteudo = descriptografar_texto(conteudo)
        print(novo_conteudo)


original = 'arquivos criados/secreto.txt'
criptografado = 'arquivos criados/criptografado.txt'

criptografar_arquivo(original, criptografado)
descriptografar_arquivo(criptografado)