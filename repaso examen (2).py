"""
Calculadora de Descuento de Comida Rápida:
El usuario debe ingresar el precio original de la comida y un cupón de descuento en porcentaje. El
programa mostrará el precio final después del descuento y el ahorro en dinero.
"""
def Funcion_Descuento ():
  print("HOLA, esto es para aplicar si descuento.")
  print(" ")
  l = float(input("coloque cuanto fue en total de su cuenta:")) #total de la cuenta
  print(" ")
  x = float(input("Coloque su cupon de descuento:"))#cupon de descuento
  print(" ")
  y = x / 100 # para convertir el porcentaje a numero decimal
  m = y * l # aplicar el descuento
  print("Esto es lo que vas a pagar:",m)
Funcion_Descuento ()
