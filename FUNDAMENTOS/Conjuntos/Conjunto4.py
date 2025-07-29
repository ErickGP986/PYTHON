'''
Unión e Intersección:

Dados set_a = {1, 2, 3} y set_b = {3, 4, 5}, muestra:

La unión (set_a | set_b).

La intersección (set_a & set_b).
'''
#creamos las tuplas
set_a = {1, 2, 3}
set_b = {3, 4, 5}

union = set_a | set_b #creamos la union
interseccion = set_a & set_b #creamos la interseccion

print(f"Las tuplas son_ {set_a} y {set_b}")#imprimimos las tuplas
print(f"La union es: {union}") #imprimimos la union
print(f"La interseccion es: {interseccion}") #imprimimimos la interseccion
