def suma(x,y):
    return x+y

def resta(n,m):
    return n-m

def multiplicacion(a,b):
    return a*b

def division(z,y):
    if y!=0:
        return z/y
    else:
        print("Y no puede ser 0")

def sumatoriaIterativa(limite):
        sum=0
        for i in range(limite):
             sum = sum + i+1
        return sum
def sumatoriaRecursiva(limite):
        if limite ==0:
             return 0
        return limite+sumatoriaRecursiva(limite-1)

#Potencia de forma recursiva e iterativa
#2**4  2*2*2*2
def potenciaIterativa(base, exponente):
    potencia =1
    if exponente == 0:
         return potencia
    for i in range(0,exponente):
        potencia = potencia*base
    return potencia
def potenciaRecursiva(base, exponente):
     if exponente==0:
          return 1
     return potenciaRecursiva(base, exponente-1)*base

def fibonacci(num1):
     if num1>1:
          return 0
     return fibonacci(num1-1)+fibonacci(num1-2)
#Fibonacci
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34