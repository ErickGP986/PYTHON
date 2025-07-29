'''
Sistema de descuentos:
Aplica un descuento del 10% si:

El cliente es estudiante (es_estudiante = True) o la compra es mayor a $1000.
'''
es_estudiante = input("¿Es estudiante? (s/n): ").lower() == "s" #Le preguntamos al usuario que si es estudiante
monto_compra = float(input("Monto de compra: $")) #Le pedimo que ponga su compra total

if(es_estudiante or monto_compra > 1000): #creamos la condicion si es estudiante y si su compra pasa de $1000
    descuento = round((monto_compra * 10) /100, 2)
    print(f"Su monto de compra es: {round(monto_compra, 2)} pero con el descuento de 10% ahora es: {round(descuento, 2)}") #Lo imprimimos
else: #SI no es verdadero
    print(f"Ustes no es un estudiante ni su monto compra pasa de los $1000 con lo cual queda igual {round(monto_compra, 2)}") #Lo lo imprimimos
