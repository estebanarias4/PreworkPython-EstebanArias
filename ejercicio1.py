#Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.
#ºF = (9/5) + 32

def convertir (Celsius):
  return (Celsius*9/5)+32
n = float (input ("Introduce los grados celsius: "))
print(f"La temperatura en grados celsius es: {convertir(n)}")