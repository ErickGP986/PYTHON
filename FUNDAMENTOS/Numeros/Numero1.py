"""""
Calculadora básica:
Pide al usuario dos números y muestra:
Suma, resta, multiplicación y división.
Potencia (n1 ** n2) y módulo/residuo (n1 % n2).
"""""""""
#Creamos las variables 
numero1 = float(input("Digite un numero: "))
numero2 = float(input("Digite un segundo numero: "))
#Hacemos los calculos
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
potencia = numero1 ** numero2
residuo = numero1 % numero2
#Lo imprimimos
print(f"La suma de los dos numeros {numero1} y {numero2} es: {suma}")
print(f"La resta de los dos numeros {numero1} y {numero2} es: {resta}")
print(f"La multiplicacion de los dos numeros {numero1} y {numero2} es: {multiplicacion}")
print(f"La division de los dos numeros {numero1} y {numero2} es: {division}")
print(f"La potencia de los dos numeros {numero1} y {numero2} es: {potencia}")
print(f"El residuo de los dos numeros {numero1} y {numero2} es: {residuo}")
