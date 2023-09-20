"""
Redacta una carta a tu ex, ponla en una variable tipo
texto, y haz que tu programa calcule el número de
palabras escritas y te despliegue el resultado.
"""
def function_carta():
  print("¿cual es tu nombre?")
  nombre = input () 
  print("escribe tu carta a tu ex",nombre)
  print(" ")
  #carta a tu ex
  texto = input ()
  palabras = texto.split()
  #cantidad de balabras
  cantidad_palabras = len(palabras)
  print(" ")
  print("este es el total de palabras:",cantidad_palabras)
function_carta ()
