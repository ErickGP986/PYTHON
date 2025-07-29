"""""
Factorial de un número:
Pide un número y calcula su factorial (ej: 5! = 5 × 4 × 3 × 2 × 1 = 120).
"""""""""
numero = int(input("Ingrese un numero: ")) #creamos la variable
fact = 1 #creamos la variable factorial

for i in range(1, numero+1): #Creamos el bucle
    fact *= i #hacemos que multiplique hasta i 
print("El factorial de ", numero, "es: ", fact) #imprimimos la variable
