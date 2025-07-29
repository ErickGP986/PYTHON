'''
Diferencia y Diferencia simétrica:

Con los mismos sets, calcula:

Elementos en set_a pero no en set_b (set_a - set_b).

Elementos que están en uno solo de los sets (set_a ^ set_b).
'''
#creamos las tuplas
set_a = {1, 2, 3}
set_b = {3, 4, 5}

diferencia = set_a - set_b #creamos la diferencia
iguales = set_a ^ set_b #creamos la diferencia simetrica

print(f"Las tuplas son_ {set_a} y {set_b}")#imprimimos las tuplas
print(f"La diferencia es: {diferencia}")#imprimimos la diferencia
print(f"Los iguales son: {iguales}")#imprimimos la diferencia simetrica
