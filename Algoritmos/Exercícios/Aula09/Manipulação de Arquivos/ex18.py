'''Suponha que você tenha um arquivo `dados.csv` com linhas no formato `nome, idade,
email`.
 - Escreva um programa que valide cada linha verificando se:
 - A idade é um número inteiro positivo.
 - O email contém um `@`.
 - Para cada linha inválida, escreva a linha em um novo arquivo chamado `erros.csv`.'''
 
import csv

entrada = 'arquivos criados/dados.csv'
saida = 'arquivos criados/erros.csv'

with open(entrada, 'r') as arquivo:
    conteudo = csv.DictReader(arquivo)

    with open(saida, 'w') as arquivo:
        for i, linha in enumerate(conteudo, start=2):
            idade_valida = False
            email_valido = '@' in linha['Email']
                        
            try:
                idade = int(linha['Idade'])
                if idade > 0:
                    idade_valida = True
                
            except ValueError:
                idade_valida = False
            
            if not idade_valida and not email_valido:
                arquivo.write(f'Linha {i} inválida. Idade e Email incorretos. {linha}\n')
            
            elif not idade_valida:
                arquivo.write(f'Linha {i} inválida. Idade incorreta. {linha}\n')
            
            elif not email_valido:
                arquivo.write(f'Linha {i} inválida. Email incorreto. {linha}\n')
            
        