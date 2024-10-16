'''Escreva uma função que verifica se uma senha
possui no mínimo 8 caracteres e pelo menos um número. Se a senha não
atender aos requisitos, levante uma exceção com uma mensagem
personalizada. Trate a exceção e mostre a mensagem ao usuário.'''

def verificaSenha(senha):
    numero = [num for num in senha if num.isdigit()]

    if len(senha) >= 8 and numero:
        return 'Senha válida.'
    else:
        raise Exception('A senha não atendeu aos requisitos')

try:
    teste = verificaSenha('aaaaaaaaa')
    print(teste)

except Exception as e:
    print(e)
