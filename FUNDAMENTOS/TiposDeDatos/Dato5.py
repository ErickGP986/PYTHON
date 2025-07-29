"""""
Formateo avanzado:
Pide al usuario su nombre, edad y ciudad.
Usa f-strings para imprimir:
"Hola [nombre], tienes [edad] años y vives en [ciudad]."
"""""""""
#Creamos las variables y se la pedimos al usuario
nombre = input("Escriba su nombre: ")
edad = input("Escriba su edad: ")
ciudad = input("Escriba su ciudad: ")
#Lo imprimimos
print(f"Hola {nombre}, tienes {edad} años y vives en {ciudad}.")
