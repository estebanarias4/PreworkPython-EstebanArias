#Escribe un programa que calcule la suma de todos los números pares del 1 al 100.

def lista_pares (n):
  return[i for i in range (n+1) if i % 2 == 0]
print(lista_pares (100))