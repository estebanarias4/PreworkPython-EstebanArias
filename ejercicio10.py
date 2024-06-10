#Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.)

numero = float(input("introduzca un numero entre 1 y 7: "))
if numero == 1:
  print("Lunes")
elif numero == 2:
  print("Martes")
elif numero == 3:
  print("Miercoles")
elif numero == 4:
  print("Jueves")
elif numero == 5:
  print("Viernes")
elif numero == 6:
  print("Sabado")
elif numero == 7:
  print("Domingo")
else:
  print(f"El día no existe")