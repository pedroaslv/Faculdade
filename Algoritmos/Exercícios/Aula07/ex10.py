'''Crie um dicionário para armazenar informações sobre estudantes, onde cada chave é o
nome de um estudante e o valor é outro dicionário contendo suas notas nas disciplinas
"Matemática", "Português" e "Ciências". Permita que o usuário acesse e altere as notas dos
alunos.'''

estudantes = {
    'Pedro': { 
        'Matemática': 10,
        'Português': 10,
        'Ciências': 10
    },
    'Douglas': { 
        'Matemática': 9.4,
        'Português': 9.9,
        'Ciências': 9.2
    },
    'Raphael': { 
        'Matemática': 8.3,
        'Português': 8.2,
        'Ciências': 8.5
    },
    'Erica': { 
        'Matemática': 7.9,
        'Português': 7.8,
        'Ciências': 7.7
    }
}


while True:
    print('-'*30)
    print('MENU')
    print('1. Acessar dicionário.')
    print('2. Alterar notas.')
    print('3. Sair.')

    opcao = input('Escolha uma opção: ')
    if opcao == '3':
        print('Sistema encerrado.')
        break

    elif opcao == '1':
        for chave, valor in estudantes.items():
            print(f'\nAluno: {chave}')
            print('Notas: ', end = '')
            for c, v in valor.items():
                print(f'{c}: {v}', end = ' | ')
            print('')
    
    elif opcao == '2':
        alunos = tuple(estudantes.keys())

        aluno = input(f'De qual aluno {alunos} gostaria de alterar a nota? ' )
        while aluno not in alunos:
            print(f'{aluno} não está no dicionário.')
            aluno = input(f'De qual aluno {alunos} gostaria de alterar a nota? ')
        
        disciplinas = tuple(estudantes[aluno].keys())

        disciplina = input(f'De qual disciplina gostaria de alterar a nota? {disciplinas}')
        while disciplina not in disciplinas:
            print(f'{disciplina} não está na relação de disciplinas.')
            disciplina = input(f'De qual disciplina gostaria de alterar a nota? {disciplinas}')
        
        nova_nota = int(input('Para qual nota deseja alterar?'))
        print('Nota alterada com sucesso!')
        estudantes[aluno][disciplina] = nova_nota
        
    
    else:
        print('Opção inválida.')