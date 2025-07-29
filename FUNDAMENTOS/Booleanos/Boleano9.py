'''
Triángulo válido:
Pide 3 longitudes y muestra True si pueden formar un triángulo (la suma de dos lados debe ser mayor que el tercero).

python
a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))
print(a + b > c and a + c > b and b + c > a)
'''
lado1 = float(input("Ingrese el Lado 1 del triangulo: ")) #le pedimo que ingrese el primer lado
lado2 = float(input("Ingrese el Lado 2 del triangulo: ")) #Le pedimos que ingrese el segundo lado
lado3 = float(input("Ingrese el Lado 3 del triangulo: ")) #Le pedimos que ingrese el tercer lado

if(lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1): #Creamos la condicion
    print("Es un trinagulo.") #decimos si es un triangulo
else:
    print("No es un triangulo.") #Decimos si no es un triangulo
