#Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.
#millas = 1*1.60934

def kilómetros (millas):
  return (millas*1.60934)
n = float (input ("Introduce una cantidad de millas: "))
print(f"la cantidad de millas introducidas equivale a {kilómetros(n)} kilometros")

