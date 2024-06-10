#Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.

def convertir_minutos (minutos):
  horas = minutos // 60
  minutos %= 60
  return f"{horas} horas y {minutos} minutos"

print(convertir_minutos(int(input("Introduce una cantidad de minutos: "))))
