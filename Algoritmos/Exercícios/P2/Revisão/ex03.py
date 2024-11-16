def adicionar_produto(lista, nome, categoria, preco, quantidade):
    lista.append({'nome':nome, 'categoria': categoria, 'preco':preco, 'quantidade':quantidade})
    print(f'Produto {nome} adicionado com sucesso!')

def atualizar_quantidade(lista, nome, quantidade):
    for produto in lista:
        if produto['nome'] == nome:
            produto['quantidade'] = quantidade
            print(f"Quantidade do produto '{nome}' alterada para {quantidade} com sucesso.")
            return
    
    print(f"Nenhum produto com o nome '{nome}' foi encontrado no cadastro.")
                
def listar_produtos(lista):
    if not lista:
        print('Nenhum produto cadastrado.')    
    
    else:
        print('Produtos cadastrados:')
        for produto in lista:
            print(f"Nome do produto: {produto['nome']}")
            print(f"Categoria: {produto['categoria']}")
            print(f"Preço: R$ {produto['preco']}")
            print(f"Quantidade: {produto['quantidade']}")
            print('-'*35)        

def ordenar_produtos(lista, chave, ordem):
    if not lista:
        print('Nenhum produto cadastrado.')    
    
    else:
        def partition(lista, inicio, fim):
            pivot = lista[fim][chave]
            
            i = inicio -1
            
            if ordem == 'crescente':
                for j in range(inicio, fim):
                    if lista[j][chave] <= pivot:
                        i+=1
                        lista[i], lista[j] = lista[j], lista[i]
            else:
                for j in range(inicio, fim):
                    if lista[j][chave] >= pivot:
                        i+=1
                        lista[i], lista[j] = lista[j], lista[i]
            
            lista[i+1], lista[fim] = lista[fim], lista[i+1]
            return i+1  
        
        def quicksort(lista, inicio, fim):
            if inicio < fim:
            
                indice_pivot = partition(lista, inicio, fim)
                quicksort(lista, inicio, indice_pivot-1)
                quicksort(lista, indice_pivot+1, fim)
            
        
        quicksort(lista, 0, len(lista)-1)
        print('Produtos ordenados com sucesso!')
        return lista
            
def salvar_estoque(lista, nome_arquivo="estoque.txt"):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write('Nome, Categoria, Preço, Quantidade\n')

            for produto in lista:
                arquivo.write(f'{produto['nome']}, {produto['categoria']}, {produto['preco']}, {produto['quantidade']}\n')
        print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")       
    
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")    
    
    except PermissionError:
        print(f"Sem permissão para gravar em '{nome_arquivo}'.")    
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}.")
    
def carregar_estoque(lista, nome_arquivo="estoque.txt"):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            
            for linha in linhas[1:]:
                nome, categoria, preco, quantidade = linha.strip().split(',')
                lista.append({'nome':nome, 'categoria': categoria, 'preco':preco, 'quantidade':quantidade})
        print(f"Arquivo '{nome_arquivo}' carregado com sucesso!")
        
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")    
    
    except PermissionError:
        print(f"Sem permissão para gravar em '{nome_arquivo}'.")    
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}.")

dados = []    

while True:
    print("Bem-vindo ao Sistema de Gestão de Estoque!")
    print("Escolha uma opção:")
    print("1. Adicionar produto")
    print("2. Atualizar quantidade")
    print("3. Listar produtos")
    print("4. Ordenar produtos")
    print("5. Salvar dados em arquivo")
    print("6. Carregar dados do arquivo")
    print("7. Sair")
    
    opcao = input(">> ")
    
    if opcao == '1':
        print('Informe os dados do produto a ser cadastrado:')
        nome = input('Nome: ')
        categoria = input('Categoria: ')
        
        while True:
            try:
                preco = float(input('Preço: R$ '))
                if preco > 0:
                    break
                
            except ValueError:
                print('Valor inválido. Informe um número positivo.')
        
        while True:
            try:
                quantidade = int(input('Quantidade: '))
                if quantidade > 0:
                    break
                else:
                    print('Informe um valor positivo.')
            except ValueError:
                print('Valor inválido. Informe um número inteiro positivo.')
            
        
        adicionar_produto(dados, nome, categoria, preco, quantidade)   
        
    
    elif opcao == '2':
        if not dados:
            print('Nenhum produto cadastrado.')
        else:
            nome = input('Qual o nome do produto que deseja alterar a quantidade?\n>> ')
            quantidade = int(input('Informe a nova quantidade: '))
            
            atualizar_quantidade(dados, nome, quantidade)
        
    elif opcao == '3':
        listar_produtos(dados)
    
    elif opcao == '4':
        while True:
            chave = input('Gostaria de ordenar por Preço ou Quantidade?\n(1) Preço\n(2) Quantidade\n> ')
            if chave in ['1', '2']:
                break
            else:
                print('Escolha uma opção válida.')
            
        while True:
            ordem = input('Em qual ordem?\n(1) Crescente\n(2) Descrente\n> ')
            if ordem in ['1', '2']:
                break
            else:
                print('Escolha uma opção válida.')
            
        chave = 'preco' if chave == '1' else 'quantidade' if chave == '2' else None
        ordem = 'crescente' if ordem == '1' else 'decrescente' if ordem == '2' else None        
        ordenar_produtos(dados, chave, ordem)
    
    elif opcao == '5':
        salvar_estoque(dados)
    
    elif opcao == '6':
        carregar_estoque(dados)
    
    elif opcao == '7':
        while True:
            salvar = input('Deseja salvar os dados antes de sair?\n(s) Sim\n(n) Não\n> ').lower()
            
            if salvar in ['s', 'n']:
                break
            else:
                print('Escolha uma opção válida.')
        if salvar == 's':
            salvar_estoque(dados)
        else:
            print('Programa encerrado!')
    
    else:
        print('Opção inválida.')