'''- Crie um programa que leia um arquivo de imagem (`imagem.jpg`) em modo binário e faça
uma cópia exata dele em `imagem_copia.jpg`.
'''

with open('arquivos criados/imagem.jpg', 'rb') as imagem:
    conteudo = imagem.read()
    
with open('arquivos criados/imagem_copia.jpg', 'wb') as backup:
    backup.write(conteudo)