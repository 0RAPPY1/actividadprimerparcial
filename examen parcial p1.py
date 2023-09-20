"""
El programa debe de permitir los precios unitarios de los componentes y calcular el costo total basado a estos precios y se debe de aplicar el 5% de descuento.
"""
def function_proyecto(): 
  print("Hola!!! estos son los precios de los siguientes componentes")
  print(" ")
  print("Aluminio: $200")
  print("Conectores: $12.5")
  print("cajas: $10")
  print(" ")
  x = float(input("Coloque el precio del aluminio:$")) #Aluminio
  v = float(input("Cantidad de cuantos quiere:")) #Cantidad del aluminio
  print(" ")
  y = float(input("Coloque el precio de los Conectores:$")) #Conectores
  o = float(input("Cantidad de cuantos quiere:")) #Cantidad de Conectores
  print(" ")
  f = float(input("Coloque el precio de las Cajas:$")) #cajas
  b = float(input("Cantidad de cuantos quiere:")) #Cantidad de cajas
  print(" ")
  can_Aluminio = x * v #Total de Aluminio
  can_Conectores = y * o # Total de conectores
  can_cajas = f * b # Total de cajas
  ñ = can_Aluminio + can_Conectores + can_cajas #total
  v = ñ * 0.05 #porsentaje
  q = ñ - v # menos el 5% 
  print("Total:",ñ,"Con el 5% de descuento:",q)
function_proyecto()
