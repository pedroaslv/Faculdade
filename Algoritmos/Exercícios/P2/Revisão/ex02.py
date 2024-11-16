import os
import datetime

def adicionar_livro(lista, titulo, autor, ano, paginas):
    lista.append({'titulo':titulo, 'autor':autor, 'ano':ano, 'paginas':paginas})
    print(f'Livro {titulo}/{autor} adicionado com sucesso!')
    
def listar_livros(lista):
    if not lista:
        print('Não há livros adicionados.')    
    else:
        print('Livros Cadastrados:')
        for livro in lista:
            print(f'Título do livro: {livro['titulo']}')
            print(f'Autor: {livro['autor']}')
            print(f'Ano de publicação: {livro['ano']}')
            print(f'Número de páginas: {livro['paginas']}')
            print('_'*35)
        
def ordenar_livros(lista, chave, ordem):
    def partition(lista, inicio, fim):
        pivot = lista[fim][chave]
        
        i = inicio - 1
        
        for j in range(inicio, fim):
            if ordem == 'crescente':
                if lista[j][chave] <= pivot:
                    i += 1
                    lista[i], lista[j] = lista[j], lista[i]
            
            elif ordem == 'decrescente':
                if lista[j][chave] >= pivot:
                    i += 1
                    lista[i], lista[j] = lista[j], lista[i]        
            
        lista[i+1], lista[fim] = lista[fim], lista[i+1]
        return i + 1
    
    def quicksort(lista, inicio=0, fim=None):
        if fim == None:
            fim = len(lista) - 1
        
        if inicio < fim:
            index_pivot = partition(lista, inicio, fim)
            quicksort(lista, inicio, index_pivot-1)
            quicksort(lista, index_pivot+1, fim)
        
    quicksort(lista)
    print(f'Os livros foram ordenados por {chave} em ordem {ordem}!')
    return lista

def salvar_livros(lista, nome_arquivo="biblioteca.txt"):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write('Titulo, Autor, Ano de Publicação, Número de Páginas\n')
            for livro in lista:
                arquivo.write(f"{livro['titulo']}, {livro['autor']}, {livro['ano']}, {livro['paginas']}\n")
        print(f"Arquivo '{nome_arquivo}' salvo com sucesso.")
        
    except FileNotFoundError:
        print('Arquivo não encontrado.')
    
    except PermissionError:
        print('Sem permissão para ler os gravar os dados no arquivo.')
    
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')

def carregar_livros(lista, nome_arquivo="biblioteca.txt"):
    try: 
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            
            for linha in linhas[1:]:
                titulo, autor, ano, paginas = linha.strip().split(',')
                lista.append({'titulo':titulo, 'autor':autor, 'ano':ano, 'paginas':paginas})
        print(f"Arquivo '{nome_arquivo}' carregado com sucesso!")
    
    except FileNotFoundError:
        print('Arquivo não encontrado.')
    
    except PermissionError:
        print('Sem permissão para ler os dados do arquivo.')
    
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')
    
                 
dados = []

while True:
    print("Bem-vindo à Biblioteca Digital!")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Ordenar livros")
    print("4. Salvar dados em arquivo")
    print("5. Carregar dados do arquivo")
    print("6. Sair")
    opcao = input("Escolha uma opção:\n")
    
    if opcao == '1':
        ano_atual = datetime.datetime.now().year
        print('Informe os dados do livro a ser adicionado:')
        titulo = input('Título: ')
        autor = input('Autor: ')
        
        while True:
            try:
                ano = int(input('Ano de Publicação: '))
                
                if ano > 0 and ano <= ano_atual:
                    break
                else:
                    print(f'Informe um ano válido. (Positivo até {ano_atual})')
                    
            except ValueError:
                print('Informe um númeiro inteiro válido para ano.')
         
        
        while True:
            try:
                paginas = int(input('Páginas: '))
                
                if paginas > 0:
                    break
                else:
                    print('Informe um número válido de páginas. (Maior que 0)')
                    
            except ValueError:
                print('Informe um númeiro inteiro positov para páginas.')
                    
        
        adicionar_livro(dados, titulo, autor, ano, paginas)
        
    elif opcao == '2':
        listar_livros(dados)
    
    elif opcao == '3':
        if not dados:
            print('Não há livros adicionados.')    
        else:
            while True:
                dicio = {'a': 'ano', 'p': 'paginas', 'c': 'crescente', 'd': 'decrescente'}
                
                chave = input('Escolha por qual chave deseja ordenar:\n(a) Para Ano\n(p) Para número de páginas\n>> ').lower()            
                if chave not in ['a', 'p']:
                    print('Opção inválida. Tente novamente.')
                    continue
                
                ordem = input('Escolha em qual ordem:\n(c) Para Crescente\n(d) Para Decrescente\n>> ').lower()
                if ordem not in ['c', 'd']:
                    print('Opção inválida. Tente novamente.')
                    continue    
                
                chave = dicio[chave]
                ordem = dicio[ordem]
                break
            
            ordenar_livros(dados, chave, ordem)
        
    elif opcao == '4':
        salvar_livros(dados)
    
    elif opcao == '5':
        carregar_livros(dados)
        
    elif opcao == '6':
        while True:
            salvar = input('Deseja salvar o arquivo antes de sair?[S/N]').upper()

            if salvar == 'S' or salvar == 'N':
                break
        
        if salvar == 'S':
            salvar_livros(dados)
        
        print('Programa encerrado.')
        break
    
    else:
        print('Opção inválida. Tente novamente.')
        
        
        
        

