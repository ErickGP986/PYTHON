'''
Invertir palabras:
Pide una frase y muestra cada palabra invertida. Ejemplo:

"Hola mundo" → "aloH odnum"
(Pista: Usa split() y slicing [::-1]).
'''
# Pedir frase al usuario
frase = input("Ingresa una frase: ")

# Invertir cada palabra
palabras_invertidas = [palabra[::-1] for palabra in frase.split()]

# Unir las palabras invertidas
resultado = " ".join(palabras_invertidas)

# Mostrar resultado
print("Frase con palabras invertidas:", resultado)
