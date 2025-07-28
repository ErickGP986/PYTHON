"""""
Variables Globales y Locales
Crea una variable global contador = 0.
Dentro de una función, incrementa contador en 1 y imprímelo.
"""""""""
contador = 0 #Creamos la variable contador
#Creamos la funcion
def myfuncion():
    global contador
    contador += 1
    print(f"Contador dentro de la funcion: {contador}")
#Usamos la funcion
myfuncion()
#Imprimimos fuera de la funcion
print(f"Contador fuera de la funcion: {contador}")
