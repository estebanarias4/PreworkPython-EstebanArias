#Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.

def cuenta_palabras (texto):
  texto_listo = texto.replace(",","")
  palabras = texto_listo.split()
  cuenta_palabras = len(palabras)
  return cuenta_palabras

texto_introducido = input("Introduce un texto: ")
resultado = cuenta_palabras (texto_introducido)

print(f"La cantidad de palabras en el texto es: {resultado}")