'''
Palíndromo:
Verifica si una palabra ingresada por el usuario es un palíndromo (se lee igual al revés, como "reconocer").

palabra = input("Ingresa una palabra: ").lower()
if palabra == palabra[::-1]:
    print("¡Es un palíndromo!")
else:
    print("No es palíndromo.")
'''
palabra = input("Ingrese una palabra: ").lower() #Le pedimos que digite una cadena y lo pasamos a minusculas
if(palabra == palabra[::-1]): #Creamos la condicion para un palindromo
    print("¡Es un palindromo!") #Lo imprimimos si es ciert
else:
    print("No es palindromo.") #En caso contrario le decimos que no es un palindromo
