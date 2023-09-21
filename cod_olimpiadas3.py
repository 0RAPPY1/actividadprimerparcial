def multi(a,b):
  x = a * b
  return x

def div(a,b):
  x = a / b
  return x 
print("Dime el primer numero: ")
a = int(input())
print("Dime el segundo numero: ")
b = int(input())

print("Este es tu multiplicacion:", multi(a,b))
print("Este es tu multiplicacion:", div(a,b))
