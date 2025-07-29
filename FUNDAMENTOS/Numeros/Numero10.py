"""""
Secuencia de Fibonacci:
Genera los primeros 10 números de la secuencia (empieza con 0, 1, 1, 2, 3, 5...).
"""""""""
def fibonnaci(numero): #Definimos la funcion con una variable como numero
    if(numero == 0 or numero == 1): #condicion para saber el numero
        return 1 #returna 1
    else:
        return fibonnaci(numero-1) + fibonnaci(numero - 2)

while True: #Creamos un ciclo con true
    n = int(input("Ingrese un numero: ")) #Le pedimos que cree un numero
 
    if(n >= 1): #Creamos la condicion 
        break #Termina 

for i in range(n): #Creamos la condicion
    print(fibonnaci(i)) #imprimimos la funcion
