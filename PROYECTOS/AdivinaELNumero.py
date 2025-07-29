"""""
Juego "Adivina el Número" 
Descripción: El programa genera un número aleatorio y el usuario debe adivinarlo.
Habilidades usadas:

Módulo random (randint).

Bucles (while).

Comparaciones lógicas (>, <, ==).
Extras:

Pistas ("es mayor/menor").

Límite de intentos (ej: 5 vidas).
"""""""""
import random #Importamoms la libreria random

intentos_maximos = 5 #creamos una variable de los intentos maximos
intentos = 0 #Otra pero esta vez igualada a cero
numero = random.randint(1,100) #Creamos la variable que va a guardar el numero aleatorio
print("Adivina el numero!, Buena suerte") #Le deseamos buena suerte al usuario
print(f"tienes {intentos_maximos} intentos para lograrlo") #Le decimos que tiene ciertos intentos para lograrlo
while (intentos < intentos_maximos): #Creamos el bucle y que termine cuando ya no tenga intentos
    numero_adivinado = int(input("Ingrese el numero a adivinar: ")) #Le decimos al usuario que adivine el numero
    intentos += 1 #a la variable le vamos sumando 1 cada vez que se equivoque
    if(numero_adivinado == numero): #Si el numero es acertado le dira que es correcto
        print(f"¡Correcto! Lo lograste en {intentos} intentos") #Le decimos que lo logro y en cuantos intentos
    elif(numero_adivinado < numero): #Si el numero es mayor que el adivinado 
        print(f"¡Es mayor!, intentos restantes: {intentos_maximos - intentos}") #Lo imprimimos y le decimos cuantos intentos le quedan
    else: #Aqui en caso contrario
        print(f"Es menor, Intentos restantes: {intentos_maximos - intentos}") #Igual pero si es menor que el adivinado

print(f"Game over El numero era {numero}.") #Y si no lo logra le decimos cual era el numero y le decimos que es game over
