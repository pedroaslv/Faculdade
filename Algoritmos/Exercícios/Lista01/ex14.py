#14. Encontrar o Maior Número em uma Lista 
#Peça ao usuário para digitar uma lista de números e exiba o maior número dessa lista.

def maior(lst):
    if len(lst) == 0:
        return None
    
    else:
        maior = 0
        for num in lst:
            if num > maior:
                maior = num
        return maior

lista = []
qtd = int(input('Quantos números deseja na lista? '))
for num in range(qtd):
    elemento = int(input(f'Digite o {num+1}º número da lista: '))
    lista.append(elemento)

print(f'A lista é: {lista} e seu maior número é: {maior(lista)}')