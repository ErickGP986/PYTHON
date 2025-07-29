'''
Contar elementos únicos:

Dada una lista de palabras ["hola", "mundo", "hola", "python"], cuenta cuántas palabras únicas hay.
'''
palabras = ["hola", "mundo", "hola", "python"] #creamos la lista

conjunto = set(palabras) #pasamos la lista a conjunto
palabras_unicas = len(conjunto) #contamos el conjunto para ver las palabras unicas

print(f"La lista es: {palabras}") #imprimmimos la lista
print(f"Las palabras son: {conjunto}") #imprimimos el conjunto
print(f"Las palabras unicas son: {palabras_unicas}") #imprimimmos las palabras unicas
