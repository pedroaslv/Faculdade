#10. Inverter uma String 
#Peça ao usuário para digitar uma string e imprima essa string de forma invertida.

frase = input('Digite uma frase: ')
fraseInv = ''
for letra in frase:
    fraseInv = letra + fraseInv

print(fraseInv)