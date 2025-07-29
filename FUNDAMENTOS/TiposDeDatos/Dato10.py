"""""
Lista de compras:
Pide al usuario 3 productos y guárdalos en una lista. Luego imprime:
"Tu lista de compras: [producto1, producto2, producto3]".
"""""""""
#Creamos las variables de productos y se las pedimos al usuario
producto1 = input("Dame un primer producto: ")
producto2 = input("Dame un segundo producto: ")
producto3 = input("Dame un tercer producto: ")
#Creamos la lista con los tres productos
lista = [producto1, producto2, producto3]
#Lo imprimimos
print(f"Tu lista de compras: {lista}.")
