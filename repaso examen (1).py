"""
Convertidor de Divisas:
El usuario debe ingresar la cantidad en dólares y el tipo de cambio actual. El programa mostrará la
cantidad equivalente en euros y en otras monedas si lo deseas.
"""
def function_Divisas():
  Dolares = float(input("Pon cantidad de dólares: "))
  print(" ")
  Total = Dolares * 0.95
  print("Esta es la convercion en Euros:",Total)
function_Divisas()
