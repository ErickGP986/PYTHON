'''
Intercambio de variables:

Intercambia los valores de a = 10 y b = 20 usando tuplas (en una sola línea):

python
a, b = b, a  # ¡Magia de las tuplas!
'''
a = 10 #creamos la primera variable
b = 20 #creamos la segunda variable

print(f"valores antes del intercambio: {a} y {b}") #imprimimos los valores

a, b = b, a #hacemos una tupla implicita

print(f"Despues de los valores del intercambio: {a} y {b}") #imprimimos los valores
