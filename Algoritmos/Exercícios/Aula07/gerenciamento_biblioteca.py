'''O sistema de gerenciamento de estoque de livros permite que a biblioteca cadastre, atualize,
remova, e busque livros, bem como verifique a quantidade de exemplares disponíveis de cada
livro. Os livros serão armazenados em uma lista, onde cada elemento é um dicionário que
representa um livro com informações como título, autor, gênero, quantidade em estoque e
código do livro. O sistema usará diversas funções para manipular a lista de dicionários.'''

def cadastrar_livro(lista, titulo, autor, genero, quantidade, codigo):
    lista.append({'Código': codigo, 'Título': titulo, 'Autor': autor, 'Gênero': genero, 'Quantidade': quantidade})
    print(f'({codigo}) {titulo} cadastrado com sucesso!')
    
def buscar_livros(lista, codigo):    
    for livro in lista:
        if livro['Código'] == codigo:
            for c, v in livro.items():
                print(f'{c}: {v}')
            return       
            
    print('Livro não encontrado.')
        
def atualizar_estoque(lista, codigo, quantidade):
    for livro in lista:
        if livro['Código'] == codigo:
            livro['Quantidade'] = quantidade
            print('Quantidade atualizada!')
            return

    print('Livro não encontrado.')

def remover_livro(lista, codigo):
    for livro in lista:
        if livro['Código'] == codigo:
            lista.remove(livro)
            print('Livro removido!')
            return

    print('Livro não encontrado.')

def listar_livros(lista):
    for livro in lista:
        for c, v in livro.items():
            print(f'{c}: {v}')
        print('=~' * 30)

def menu():
    livros = []
    while True:
        print('='*50)
        print('SISTEMA DE GERENCIAMENTO DE BIBLIOTECA')
        print('='*50)
        print('1. Cadastrar Livro.')
        print('2. Buscar Livro.')
        print('3. Atualizar Estoque')
        print('4. Remover Livro')
        print('5. Listar Todos os Livros.')
        print('6. Sair.')

        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            titulo = input('Informe o Titulo do Livro: ')
            autor = input('Informe o Autor: ')
            genero = input('Informe o Gênero: ')
            quantidade = input('Informe a Quantidade em Estoque: ')
            codigo = input('Informe o Código: ')
            cadastrar_livro(livros, titulo, autor, genero, quantidade, codigo)
        
        elif not livros and opcao in ['2', '3', '4', '5']:
            print('Nenhum livro cadastrado.')        
         
        elif opcao == '2':
            codigo = input('Informe o código do livro que está buscando: ') 
            buscar_livros(livros, codigo)

        elif opcao == '3':
            codigo = input('Informe o código do livro: ') 
            quantidade = input('Informe a quantidade de Estoque: ')
            atualizar_estoque(livros, codigo, quantidade)            

        elif opcao == '4':
            codigo = input('Informe o código do livro que deseja remover: ') 
            remover_livro(livros, codigo)

        elif opcao == '5':
            listar_livros(livros)
        
        elif opcao == '6':
            print('Sistema encerrado.')
            break
    
        else:
            print('Opção inválida.')

menu()

