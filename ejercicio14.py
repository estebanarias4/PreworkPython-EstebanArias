#Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.

precio = float(input("Indique el precio del producto: "))
a = (precio * 20)/100
total = precio - a
print(f"El precio total a pagar es: {total}")