'''
Crear y modificar listas:

Crea una lista llamada frutas con los valores ["manzana", "banana", "naranja"].

Añade "uva" al final.

Elimina "banana".

Imprime la lista resultante.
'''
frutas = ["Manzana", "banana", "naranja"] #Creamos la lista
print(f"Lista original: {frutas}") #Imprimimos la lista original

frutas.append("uva") #Añadimos uva al final de la lista
print(f"Lista añadiendo uva: {frutas}") #La imprimimos

frutas.remove("banana") #eliminamos banana de la lista
print(f"La lista eliminando banana: {frutas}") #lo imprimimos

print(f"--Lista resultante-- {frutas}") #Imprimimos la lista resultante
