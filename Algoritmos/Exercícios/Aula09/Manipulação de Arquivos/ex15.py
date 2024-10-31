''' - Escreva um programa que permita ao usuário registrar informações (nome, idade, email)
em um arquivo `usuarios.txt`.
 - Cada vez que o programa for executado, ele deve adicionar um novo registro ao arquivo.'''
 
with open('arquivos criados/usuarios.txt', 'a') as arquivo:
    nome = input('Nome: ')
    idade = input('Idade: ')
    email = input('Email: ')
    
    arquivo.write(f'{nome}, {idade}, {email}\n')
    