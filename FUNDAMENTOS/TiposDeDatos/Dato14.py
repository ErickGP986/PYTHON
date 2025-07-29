"""""
Buscar en diccionario:
Dado el diccionario:
estudiante = {"nombre": "Ana", "curso": "Python", "nota": 85}  
Pide al usuario una clave (ej: "curso") e imprime su valor o "Clave no encontrada" si no existe.
"""""""""
estudiante = {"nombre" : "Ana", "curso" : "Python", "nota" : 85} #Creamos el diccionario

# Pedir al usuario una clave
clave = input("Ingresa la clave a buscar (ej: 'curso'): ")

# Buscar e imprimir el valor (o mensaje de error)
valor = estudiante.get(clave, "Clave no encontrada")
print(f"Valor: {valor}")
