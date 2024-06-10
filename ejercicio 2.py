#Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.

precio = float(input("Indique el total de la cuenta: "))
propina = precio * 0.15
total= precio + propina
print(f"el total de la cuenta es: {total}")