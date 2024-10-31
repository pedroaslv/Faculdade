'''Crie um programa que faça uma cópia de segurança do conteúdo de um arquivo `dados.txt`
em um arquivo de log chamado `backup.txt`.
 - No final de cada execução, adicione a data e a hora em que a cópia de segurança foi feita.'''
 
import datetime

arquivo_original = 'arquivos criados/dados.txt'
arquivo_backup = 'arquivos criados/backup.txt'

with open(arquivo_original, 'r') as arquivo:
    conteudo = arquivo.read()
    
with open(arquivo_backup, 'a') as arquivo:
    agora = datetime.datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y - %H:%M")
    arquivo.write(f'{data_formatada} - Cópia de segurança realizada.\n')

