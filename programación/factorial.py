#factorial sin utilizar signos

#5!->  factorial 5*4*3*2*1 = 120

def factorial(num):
    acum=1
    #range(6)= [0,1,2,3,4,5]
    for x in range(num):
        acum = acum*(x+1)
    return acum


    #factorial sin utilizar signos


x= int (input("ingrese numero 1"))

print("el resultado es, factorial" (acum))