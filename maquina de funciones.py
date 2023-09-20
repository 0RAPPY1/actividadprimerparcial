#primer valor
def f(x): 
  f_x= -abs(3*x)
  return f_x

y = f(10) 

#el segundo valor
def g(x): 
  g_x= (-2*x+34)
  return g_x

c= g(10) 

#el tercer valor
def H(x): 
  H_x= (-x/3-10)
  return H_x
I = H(10) 

# cuarto valor 
def J(x): 
  J_x= (x-2)**2
  return J_x
F = J(10) 

#Total de todos los valores
print ("1=",y,",2=",c,",3=",I,",4=",F)
