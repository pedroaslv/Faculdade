import os

def adicionar_aluno(lista, nome, notas):    
    media = sum(notas) / len(notas)
    lista.append({'Nome': nome, 'Notas': notas, 'Media': media})
    print(f'Aluno {nome} adicionado com sucesso!')


def ordenar_alunos(lista, crescente=True, chave='Media'):
    def partition(lista, inicio, fim):
        pivot = lista[fim][chave]
        
        i = inicio - 1
        
        for j in range(inicio, fim):         
            if crescente:    
                if lista[j][chave] <= pivot:
                    i +=1
                    lista[i], lista[j] = lista[j], lista[i]
            else:
                if lista[j][chave] >= pivot:
                    i +=1
                    lista[i], lista[j] = lista[j], lista[i]
        lista[i+1], lista[fim] = lista[fim], lista[i+1]
        return i+1
            
    def quicksort(lista, inicio=0, fim=None):
        if fim == None:
            fim = len(lista) - 1
            
        if inicio < fim:
            index_pivot = partition(lista, inicio, fim)
            quicksort(lista, inicio, index_pivot-1)
            quicksort(lista, index_pivot+1, fim)
    
    quicksort(lista)
    return lista
        


def salvar_em_arquivo(lista, nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(f'Aluno, Média\n')
            for aluno in lista:
                arquivo.write(f"{aluno['Nome']}, {aluno['Media']}\n")
        print(f"Arquivo {nome_arquivo} salvo com sucesso.")
    except PermissionError:
        print(f"Permissão negada para escrever no '{nome_arquivo}'.")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")  
    

def exibir_alunos(lista):
    if not lista:
        print('Ainda não há alunos adicionados.')
    else:
        for aluno in lista:
            print(f'Nome do Aluno: {aluno['Nome']}\nNotas: {aluno['Notas']}\n\n')

dados = []
while True:
        print("Menu:")
        print("1. Adicionar aluno")
        print("2. Visualizar Lista e Sair do Programa")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input('Nome do aluno: ')
            
            while True:
                try:
                    qtd = int(input('Quantas notas deseja adicionar? (Min 2 e Max 5) '))

                    if qtd >=2 and qtd <= 5:
                        break
                    else:
                        print('Quantidade inválida. Informe um valor entre 2 e 5.\n')
                
                except ValueError:
                    print('Valor inválido. Insira um valor numérico.\n')

            notas = []
            for i in range(qtd):
                while True:
                    try:
                        nota = float(input(f'Insira a {i+1}ª nota (0 a 10):\n'))
                        
                        if nota >= 0 and nota <= 10:
                            break
                        else:
                            print('Nota inválida. Tente novamente com um número entre 0 e 10.\n')
                    
                    except ValueError:
                        print('Valor inválido. Insira um valor numérico.\n')
                    
                
                notas.append(nota)
            adicionar_aluno(dados, nome, notas)

        elif opcao == '2':
            ordenar_alunos(dados, False)
            exibir_alunos(dados)
            
            nome_arquivo = input('Qual o nome do arquivo deseja salvar? ') + '.txt' #'alunos.txt'
            
            if os.path.exists(nome_arquivo):
                while True:
                    try:                    
                        opcao = input('Já existe um arquivo com esse nome. Deseja sobrescrever? [S/N]').capitalize()
                        
                        if opcao == 'S' or opcao == 'N':
                            break
                        else:
                            print('Escolha uma opção válida. [S/N]')
                    except Exception as e:
                        print(f"Ocorreu um erro inesperado: {e}. Tente novamente")
                
                if opcao == 'S':
                    salvar_em_arquivo(dados, nome_arquivo)
                    print(f"Os dados foram salvos no arquivo '{nome_arquivo}'.")
                elif opcao == 'N':
                    print('O arquivo não foi sobrescrito.')
                    break
                print('Programa encerrado.')
                break

        else:
            print('Escolha uma opção válida.')
        
        



