"""""
Operaciones con listas:
Crea una lista con los números [5, 10, 15, 20] y:
Añade el número 25 al final.
Elimina el número 10.
Ordena la lista en reversa.
"""""""""
lista = [5, 10, 15, 20] #Creamos la lista 
print(f"Lista original: {lista}") #lo imprimimos
lista.append(25) #Le añadimos el 25 al final
print(f"añadirle 25 a lista: {lista}") #Lo imprimimos
lista.remove(10) #Le eliminamos el 10 a la lista
print(f"eliminar el 10 de la lista: {lista}") #Lo imprimimos
lista.sort(reverse=True) #Lo ponemos en orden inverso
print(f"Poner la lista en orden inverso: {lista}") #Lo imprimimos
