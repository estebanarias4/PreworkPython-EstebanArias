#Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.

palabra = input("introduzca una palabra: ")
vocales="aeiouAEIOU"
n = 0
for i in palabra:
  if i in vocales:
    n=n+1
print(f"la cantidad de vocales en la frase es {n}")


