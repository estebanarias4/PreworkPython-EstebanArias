# Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona
#IMC = Peso(kg/estatura (m2))

peso =float(input("Indica tu peso: "))
altura = float(input("Indica tu altura en m2:" ))
imc = peso / altura
print(f"tu indice de masa corporal es: {imc}")