'''
Buscador de palabras comunes:

Dados dos textos (strings), conviértelos a sets de palabras y muestra las palabras que se repiten en ambos.
'''
texto1 = input("Introduce un texto: ") #le pides el primer texto
texto2 = input("Introduce un segundo texto: ") #le pides el segundo del tetxo

set1 = set(texto1.lower().split()) #convertimos el primer texto a set
set2 = set(texto2.lower().split()) #convertimos el segundo texto a set

palabras_comunes = set1 & set2 #lo hacemos interceccion
#lo imprimimos
print("Palabras comunes son:")
print(palabras_comunes)
