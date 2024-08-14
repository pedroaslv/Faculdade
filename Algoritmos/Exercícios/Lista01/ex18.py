#18. Simulação de Lançamento de Moeda 
#Crie um programa que simule o lançamento de uma moeda (cara ou coroa) e exiba o resultado.

import random
import time

def escrever_devagar(texto,tempo):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(tempo)    

moeda = random.choice(['CARA', 'COROA'])

escrever_devagar('Lançando moeda...',0.1)

print(f'\nA moeda lançada foi: ')
time.sleep(0.5)
print(moeda)