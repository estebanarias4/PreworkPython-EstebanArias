#Crea un programa que realice operaciones aritméticas simples (suma, resta,multiplicación, división) según la elección del usuario.

a = int(input("ingrese un numero: "))
b = int(input("ingrese otro numero: "))
operacion = input("eliga una operacion: ")
if operacion == "suma":
  print(f"La suma es: {a + b}")
elif operacion == "resta":
  print(f"La resta es: {a - b}")
elif operacion == "multiplicacion":
  print(f"La multiplicacion es: {a * b}")
elif operacion == "division":
  print(f"La division es: {a / b}")