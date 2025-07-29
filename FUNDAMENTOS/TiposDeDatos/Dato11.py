"""""
 Inmutabilidad:
- Crea una tupla con los días de la semana. Intenta modificar el primer elemento (debe dar error).
"""""""""
#Creamos la tupla
myTupla = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
#La mostramos originalmente
print(myTupla)

try:
    myTupla[0] = "Monday"  # Intento de modificación
except TypeError as e: #Manejo de error
    print(f"\nError al intentar modificar la tupla: {e}")
    print("Las tuplas son inmutables y no permiten cambios después de su creación.")
#Imprimir el resultado
print("\nTupla después del intento de modificación:", myTupla)
