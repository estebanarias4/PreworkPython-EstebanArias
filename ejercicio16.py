#Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.

lista_numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
par = 0
impar = 0
for x in lista_numeros:
  if x % 2 == 0:
    par += 1
  else:
    impar += 1
print(f"El total de numeros pares es: ", par)
print(f"el total de numeros impares es: ", impar)