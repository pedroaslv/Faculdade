#16. Contagem Regressiva 
#Escreva um programa que faça uma contagem regressiva de 10 a 0, imprimindo os números na tela.

import time

for num in range(10,-1,-1):
    print(num)
    time.sleep(0.3)