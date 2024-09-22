''' Dada uma lista de nomes de alunos e suas respectivas notas em uma prova, crie um
dicionário e permita que o usuário consulte e atualize a nota de um aluno específico.'''

alunos = ['Pedro', 7, 'Douglas', 8, 'Raphael', 8, 'Erica', 10]

dicio = {}

for i, v in enumerate(alunos):
    if i % 2 == 0:
        dicio.update({v: alunos[i+1]})    


while True:
    print('='*20)
    print('MENU')
    print('1. Consultar dicionário.')
    print('2. Atualizar uma nota.')
    print('3. Sair.')

    opcao = input('Escolha uma opção: ')
    if opcao == '3':
        print('Programa finalizado.')
    
    elif opcao == '1':
        print(f'Este é o dicionário: {dicio}')
    
    elif opcao == '2':
        aluno = list(dicio.keys())
        aluno_escolhido = input(f'Informe de qual aluno {aluno} gostaria de alterar a nota: ')
        while aluno_escolhido not in aluno:
            print('Aluno não está no dicionário. Tente novamente.')
            aluno_escolhido = input(f'Informe de qual aluno {aluno} gostaria de alterar a nota: ')
        nova_nota = int(input('Atualizar para qual nota? '))
        dicio.update({aluno_escolhido:nova_nota})
    
    else:
        print('Opção inválida.')
            
        
    