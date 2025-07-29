'''
Palabras únicas en un texto

Dado un párrafo, convierte las palabras en un set.

Imprime cuántas palabras únicas contiene.
'''
texto = input("Ingrese un parrafo: ") #pedimos el parrafo al usuario

numero_str = texto.lower().split() #convertimos el texto en minusculas y separarlas por espacio

palabras_unicas = set(numero_str) #buscamos las palabras unicas
print(F"Las palabras unicas son: {palabras_unicas}") #imprimimos las palabras unicas
print(f"La cantidad de palabras unicas son: {len(palabras_unicas)}") #imprimimos la cantidad de palabras unicas
