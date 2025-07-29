'''
Analizador de palabras únicas

El programa pide al usuario un texto.

Muestra cuántas palabras únicas tiene.

Muestra las palabras ordenadas alfabéticamente.
'''
texto = input("Digite un texto: ") #le pedimos el texto al usuario

texto = texto.lower() #hacemos el texto a minusculas
palabras = texto.split() #separamos las palabras por espacio


palabras_unicas = set(palabras) #buscamos las palabras unicas

print(f"Numero de palabras unicas: {len(palabras_unicas)}") #contamos el numero de palabras unicas

palabras_ordenadas = sorted(palabras_unicas) #ordenamos las palbras unicas
print("palabras_unicas ordenadas alfabeticamente:") 
for palabras in palabras_unicas:
    print(palabras_unicas) #imprimimos las palabras alfabeticamente
