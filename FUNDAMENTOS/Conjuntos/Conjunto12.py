'''
Agregar y eliminar elementos

Crea un set vacío.

Añade los elementos 10, 20 y 30.

Elimina 20 usando remove().

Usa discard() para intentar eliminar 40 (observa que no lanza error).
'''
vacio = set() #creamos un set vacio
#le añadimos al set los numeros
vacio.add(10)
vacio.add(20)
vacio.add(30)
print(f"Los numeros son: {vacio}") #imprimimos los numeros

vacio.remove(20) #removemos el numero 20
print(f"numeros eliminando 20: {vacio}") #imprimimos el set

vacio.discard(40) #usamos discard para 40
print(f"Los numeros con discard: {vacio}") #imprimimos la variable
