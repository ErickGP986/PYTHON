"""""
Variables y Listas
Crea una lista con 3 números ingresados por el usuario.
Calcula el promedio y muestra el mayor y menor número.
"""""""""
# Crear una lista vacía para almacenar los números
numeros = []

# Pedir al usuario que ingrese 3 números y agregarlos a la lista
for i in range(3):
    numero = float(input(f"Ingresa el número {i + 1}: "))
    numeros.append(numero)

# Calcular el promedio
promedio = sum(numeros) / len(numeros)

# Encontrar el mayor y menor número
mayor = max(numeros)
menor = min(numeros)

# Mostrar los resultados
print("\nResultados:")
print(f"Lista de números: {numeros}")
print(f"Promedio: {promedio:.2f}")  # Mostrar con 2 decimales
print(f"Mayor número: {mayor}")
print(f"Menor número: {menor}")
