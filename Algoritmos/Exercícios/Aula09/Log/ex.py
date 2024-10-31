'''Crie um programa que registre eventos em um sistema fictício e os grave em um
arquivo de log chamado sistema_log.txt. Cada evento deve registrar a data e hora em que
ocorreu, além de uma breve descrição fornecida pelo usuário. A cada execução do programa, o
usuário poderá escolher entre registrar um novo evento ou visualizar todos os eventos já
registrados.
1. Passo 1: Peça ao usuário para inserir uma descrição do evento ou para visualizar o log
completo.
2. Passo 2: Se o usuário optar por registrar um evento, salve a descrição no arquivo
sistema_log.txt, juntamente com a data e hora atuais.
3. Passo 3: Se o usuário optar por visualizar o log, exiba o conteúdo do arquivo no console.
4. Passo 4: Certifique-se de tratar possíveis exceções, como a ausência do arquivo de log.'''

import datetime

caminho = 'sistema_log.txt'

def registrar_evento(evento):
    agora = datetime.datetime.now()
    data_formatada = agora.strftime('%d/%m/%Y %H:%M:%S')
    
    with open(caminho, 'a') as arquivo:
        arquivo.write(f'{data_formatada} - Evento: {evento}\n')
    
    print('Evento registrado no log.')
    
def visualizar_log():
    try:
        with open(caminho, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print('O arquivo de Log não existe.')
        
def limpar_log():
    with open(caminho, 'w') as arquivo:
        pass
    print('Log limpo.')

while True:
    print('SISTEMA FICTÍCIO')
    print('1. Registrar um Evento.')
    print('2. Visualizar o Log.')
    print('3. Limpar Log.')
    print('4. Sair.')
    
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        evento = input('Informe um evento: ')
        registrar_evento(evento)
    
    elif opcao == '2':
        visualizar_log()
    
    elif opcao == '3':
        limpar_log()        
    
    elif opcao == '4':
        registrar_evento('Logout do usuário.')
        print('Sistema encerrado.')
        break

    else:
        print('Escolha um opção válida.')
    

