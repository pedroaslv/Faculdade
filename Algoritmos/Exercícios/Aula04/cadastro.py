clientes = {}

def adicionar_cliente(nome, email, telefone, endereco):
    if email not in clientes:
        clientes[email] = {"nome":nome, "telefone":telefone, "endereco":endereco }
        print(f'Cliente com o e-mail "{email}" cadastrado com sucesso.')
        #chave principal sendo o email por se tratar do dado mais importante e que não aceitará repetição
    else:
        print('Não foi possível realizar o cadastro, e-mail já está cadastrado.')
        

def exibir_clientes():
    if len(clientes) ==0:
        print('Não há clientes cadastrados.')
    else:
        c = 1
        for chave, dado in clientes.items():
            print(f'Cliente {c}\nNome: {dado['nome']} | Email: {chave} | Telefone: {dado['telefone']} | Endereço: {dado['endereco']}')
            print('~='*50)
            c+=1
            
def buscar_cliente(email):
    for chave, dado in clientes.items():
        if email == chave:
            print('Cliente encontrado!')
            print(f'Nome: {dado['nome']} | Email: {chave} | Telefone: {dado['telefone']} | Endereço: {dado['endereco']}')
            return
    
    print('Cliente com o e-mail informado não está cadastrado.')
       
def remover_cliente(email):
    for chave in clientes.keys():
        if email == chave:
            clientes.pop(chave)
            print(f'Cliente com o e-mail "{email}" removido com sucesso!')
            return
    
    print('Cliente com o e-mail informado não está cadastrado.')  

def testar():
    adicionar_cliente('pedro','pedro@email.com','22 1234-5678','Rua Alpha')
    adicionar_cliente('douglas','douglas@email.com','22 8765-4321','Rua Bravo')
    adicionar_cliente('mariana','mariana@email.com','22 4321-8765','Rua Charlie')
    exibir_clientes()
    buscar_cliente('douglas@email.com')
    remover_cliente('douglas@email.com')
    exibir_clientes()
    
def menu():
    while True:        
        print('~='*20)
        print('SISTEMA DE CADASTRO DE CLIENTES')
        print('~='*20)
        print('1. Cadastrar Clientes')
        print('2. Exibir Clientes')
        print('3. Buscar Cliente')
        print('4. Remover Cliente')
        print('5. Sair')     
                    
        opcao = input('Escolha uma opção: ')        
        if opcao == '1':
            email = input('EMAIL: ')
            nome = input('NOME: ')            
            telefone = input('TELEFONE: ')
            endereco = input('ENDEREÇO: ')
            adicionar_cliente(nome, email, telefone, endereco)                            
        
        elif opcao == '2':
            exibir_clientes()
        
        elif opcao == '3':
            email = input('Informe o e-mail que deseja buscar: ')
            buscar_cliente(email)
            
        elif opcao == '4': 
            email = input('Informe o e-mail que deseja remover: ')
            remover_cliente(email)
               
        elif opcao == '5':
            print('Sistema encerrado.')
            break
        else:
            print('Opção inválida.')

#testar()
menu()




