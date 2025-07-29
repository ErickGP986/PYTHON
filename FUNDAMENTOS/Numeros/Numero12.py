"""""
Número primo:
Pide un número y determina si es primo (solo divisible entre 1 y sí mismo).
"""""""""
n = int(input("Ingrese un numero: ")) #creamos ka variable y se la pedimos al usuario
x = 1 #creamos la variable y la igualamos a 1
c = 0 #igual con 0
#Creamos el bucle
while x <= n: #condicion de while
    if n % x == 0: #Creamos la condicion de division y que su residuo sea 0
     c = c + 1 #le sumamos 1 a c
    x = x + 1 #le sumamos a x 1
if c == 2: #Creamos la condicion que c sea igual a 2
   print(f"El numero {n} es primo") #imprimimos si, si es primo
else:
   print(f"El numero {n} no es primo") #Imprimos si, no es primo
