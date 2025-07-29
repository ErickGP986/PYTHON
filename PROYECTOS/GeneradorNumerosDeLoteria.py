'''
Generador de números de lotería:

Usa un set para generar 6 números aleatorios únicos entre 1 y 50 (usa random.sample).
'''
import random #importamos la libreria random

numero_loteria = set(random.sample(range(1, 51), 6)) #creamos los digitos de loteria

print(f"numero de loteria: {numero_loteria}") #lo imprimimos
