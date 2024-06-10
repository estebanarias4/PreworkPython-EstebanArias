#Crea un programa que sume todos los números en una lista ingresada por el usuario.

numeros = list(map(int,input("Introduce una lista de numeros separados por un espacio: "). split()))

print(f"la suma de los numeros introducidos es = {sum(numeros)}")