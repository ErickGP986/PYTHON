"""""
Comparaciones lógicas:
Pide dos números y muestra:
Si son iguales.
Si el primero es mayor que el segundo.
Si ambos son positivos (mayores a 0).
"""""""""
#Creamos las variables y se las pedimos al usuario
num1 = int(input("Digite un primer numero: "))
num2 = int(input("Digite un segundo numero: "))
#Creamos las condiciones y lo imprimimos segun la expresion
if num1 == num2:
    print("Los numeros son iguales.")
else:
    print("Los numeros son diferentes.")
if num1 > num2:
    print(f"El nuemro {num1} es mayor que {num2}.")
else:
    print(f"El numero {num2} es mayor que {num1}.")
if num1 > 0 and num2 > 0:
    print("Ambos numeros son positivos.")
