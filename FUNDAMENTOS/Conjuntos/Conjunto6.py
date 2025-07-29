'''
Subconjuntos:

Dados set_x = {1, 2} y set_y = {1, 2, 3, 4}, verifica si set_x es subconjunto de set_y (usa .issubset()).
'''
#creamos los conjuntos
set_x = {1, 2}
set_y = {1, 2, 3, 4}
subconjunto = set_x.issubset(set_y) #vemos si x es subconjunto de y

print(f"El set x es: {set_x}")#imprimimos el conjunto de x
print(f"El set y es: {set_y}")#imprimimos el conjunto de y
print(f"El subconjunto es: {subconjunto}") #vemos si x es subconjuunto de y
