#Escribe un programa que determine si un número ingresado por el usuario es primo o no.

n = int(input("Introduzca un numero: "))
x = 1
y = 0
while x <= n:
  if n % x == 0:
    y = y + 1
  x = x + 1
if y == 2:
  print(f"El numero {n} es primo")
else:
  print(f"El numero {n} no es primo")