#função de cadastro agora gerando o código de maneira automática
def cadastrar_projeto(lista, cliente, gerente, data, status):
    if not lista:
        codigo_final = 'P001'
    
    else:
        codigo = str(max([int(projeto['Código'].replace("P","")) for projeto in lista]) + 1)
        codigo_final = 'P' + '0' * (3-len(codigo)) + codigo
        
    lista.append({'Código': codigo_final, 'Cliente': cliente, 'Gerente': gerente, 'Data_Inicial': data, 'Status': status})
    print(f'Projeto {codigo_final} cadastrado com sucesso.')


def atualizar_status_projeto(lista, codigo, status):
    for projeto in lista:
        if projeto['Código'] == codigo:
            projeto['Status'] = status
            print(f'Status do projeto {codigo} atualizado para {status} com sucesso.')
            return
        
    print(f'Projeto {codigo} não encontrado.')


def buscar_projeto(lista, codigo):
    for projeto in lista:
        if projeto['Código'] == codigo:
            print(f'{'='*30}\nPROJETO LOCALIZADO:\nCódigo: {projeto['Código']}\nCliente: {projeto['Cliente']} | Gerente: {projeto['Gerente']} | Data Inicial: {projeto['Data_Inicial']} | Status: {projeto['Status']}')
            return   
        
    print(f'Projeto {codigo} não encontrado.')
    
def listar_projetos(lista):
    if not lista:
        print('Não há nenhum projeto cadastrado.')
    
    print('PROJETOS CADASTRADOS:')
    for projeto in lista:
        print('='*30)
        for chave, valor in projeto.items():
            print(f'{chave}: {valor}')

def contar_projetos_por_gerente(lista, gerente):
    c = 0
    for projeto in lista:
        if projeto['Gerente'] == gerente:
            c += 1
    
    if c == 0:
        print(f'Não foi localizado nenhum projeto para o(a) gerente {gerente}.')
    
    elif c > 1:
        print(f'O(a) gerente {gerente} possui {c} projetos.')
    else:
        print(f'O(a) gerente {gerente} possui {c} projeto.')
            
projetos = []

def testes():
    cadastrar_projeto(projetos, "Cliente A", "Gerente X", "2024-01-01", "Planejamento")
    cadastrar_projeto(projetos, "Cliente B", "Gerente Y", "2024-02-01", "Em Andamento")
    cadastrar_projeto(projetos, "Cliente C", "Pedro", "2024-09-24", "Planejamento")
    atualizar_status_projeto(projetos,"P002", "Concluído")
    atualizar_status_projeto(projetos,"P005", "Concluído")
    buscar_projeto(projetos, "P004")
    buscar_projeto(projetos,"P005")
    listar_projetos(projetos)
    contar_projetos_por_gerente(projetos,"Pedro")

    
def menu():
    while True:
        print('-'*45)
        print('BEM VINDO AO SISTEMA DE GESTÃO DE PROJETOS')
        print('-'*45)
        print('1. Cadastrar Projeto')
        print('2. Atualizar Status de um Projeto')
        print('3. Buscar Projeto')
        print('4. Listar Projetos Cadastrados')
        print('5. Contar Projetos de um Gerente')
        print('6. Sair')
        
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            cliente = input('Informe o Cliente do Projeto: ')
            gerente = input('Informe o Gerente do Projeto: ')
            data = input('Informe data Inicial o Projeto: ')
            status = input('Informe o Status atual do Projeto: ')
            
            cadastrar_projeto(projetos, cliente, gerente, data, status)
        
        elif opcao == '2':
            codigo = input('Informe o Código do Projeto que deseja atualizar: ').capitalize()
            status = input('Informe o novo Status: ')
                        
            atualizar_status_projeto(projetos, codigo, status)
        
        elif opcao == '3':
            codigo = input('Informe o Código do Projeto que deseja buscar: ').capitalize()
            buscar_projeto(projetos, codigo)

        elif opcao == '4':
            listar_projetos(projetos)
        
        elif opcao == '5':
            gerente = input('Informe o Gerente do Projeto: ')
            contar_projetos_por_gerente(projetos, gerente)
        
        elif opcao == '6':
            print('Programa encerrado.')
            break
        
        else:
            print('Escolha uma opção válida.')

menu()