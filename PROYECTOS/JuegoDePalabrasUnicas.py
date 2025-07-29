'''
Juego de palabras únicas

El usuario ingresa una lista de palabras.

El programa verifica cuántas son únicas.

Podrías agregar puntaje si quieres gamificarlo.
'''
while True: #creamos un bucle while para que se repita simepre
    print("\t---juego de palabras unicas---") #le decimos que es un juego de palabras unicas
    opcion = input("Desea jugar (s/n): ").lower() #le decimos si quiere jugar
    
    if(opcion == 's'): #si, si 
     texto = input("Ingrese un parrafo: ") #le pedimos que ingrese un tetxo

     palabras = texto.lower().split() #ponemos el parrafo en minusculas y los separamos por espacio

     palabras_unicas = set(palabras) #vemos cuales con las palabras unicas
     
     print(f"Tu texto es: {texto}") #vemos cual es el texto
     print(f"Las palabras_unicas son: {palabras_unicas}") #le decimos cuales fueron sus palabras unicas
     print(f"puntaje: {len(palabras_unicas)}") #contamos cuantas tiene para ver cual es el puntaje
    else: #si no
        print("El juego ah terminado.") #le decimos que el juego ya termino
        break #y terminamos el bucle
