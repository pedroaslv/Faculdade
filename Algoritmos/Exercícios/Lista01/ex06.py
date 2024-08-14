#6. Converter Celsius para Fahrenheit 
#Escreva um programa que converta uma temperatura de graus Celsius para Fahrenheit.

def conversor_CF(celsius):
    fah = celsius * 1.8 + 32
    return f'Uma temperatura de {celsius}°C equivale a {fah}°F.'

print(conversor_CF(15))