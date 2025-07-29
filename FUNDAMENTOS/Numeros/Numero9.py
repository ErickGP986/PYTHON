"""""
Separar número en dígitos:
Pide un número entero (ej: 1234) y sepáralo en dígitos individuales (ej: [1, 2, 3, 4]).
(Pista: Convierte a str y luego a int).
"""""""""
numeros = [] #Creamos la lista
def separar(x): #definimos la funcion separar
    while x > 0: #Creamos el buecle
     print(x % 10) #imprimimos
     numeros.append(x % 10) #lo añadimos a la lista
     x = x // 10 #x = x 
    print(numeros[:]) 

n = int(input("Digite una lista de numeros: ")) #Creamos la variable
separar(n) #Llamamos a la funcion
