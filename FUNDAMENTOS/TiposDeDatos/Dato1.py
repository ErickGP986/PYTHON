"""""
Operaciones básicas:
Pide al usuario dos números enteros y muestra:
La suma.
La diferencia (resta del mayor menos el menor).
El producto.
La división (redondeada a 2 decimales).
"""""""""
#creamos las variables y se las pedimos al usuario
numero1 = int(input("Escriba un primer numero: "))
numero2 = int(input("Escriba el segundo numero: "))

suma = numero1 + numero2 #hacemos la operacion de la suma

diferencia = int #Creamos la variable de diferencia
#Hacemos la condicion de numero para asi sacar la resta y restar el mayor ante el menor
if(numero2 > numero1):
    diferencia = numero2 - numero1
else:
    diferencia = numero1 - numero2

producto = numero1 * numero2 #hacemos la operacion de multiplicacion

division = numero1 / numero2 #Creamos la operacion de division
#Imprimimos el resultado
print(f"Los numeros son: {numero1} y {numero2}")
print(f"La suma de los dos numeros es: {suma}")
print(f"La diferencia de los dos numeros es: {diferencia}")
print(f"El producto de los dos numeros es: {producto}")
print(f"La division de los dos numeros es: {division:.2}")
