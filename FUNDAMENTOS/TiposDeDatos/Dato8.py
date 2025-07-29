"""""
Edad para votar:
Pide la edad del usuario e imprime True si puede votar (edad ≥ 18) y False si no.
"""""""""
edad = int(input("Escriba su edad: ")) #Le pedimos la edad al  usuario
votar = bool #creamos la variable booleana
if edad >= 18: #creamos la condicion de votar y listo
    votar = True
    print("Usted puede votar: ", votar)
else:
    votar = False
    print("Usted puede votar: ", votar)
