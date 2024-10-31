'''Crie um programa que simule uma transferência
bancária. Peça ao usuário o saldo da conta e o valor da transferência. Caso o
saldo seja insuficiente, levante uma exceção do tipo ValueError com a
mensagem "Saldo insuficiente". Trate a exceção adequadamente e informe o
usuário'''

try:
    saldo = float(input('Infore o saldo da sua conta bancária: R$ '))
    valor_transferencia = float(input('Informe o valor que deseja transferir: R$ '))

    if valor_transferencia > saldo:
        raise Exception('Saldo insuficiente.')

    else:
        print(f'Transferência de R$ {valor_transferencia} realizada com sucesso.')

except ValueError:
    print('Valor inserido não é um número.')

except Exception as e:
    print(e)
