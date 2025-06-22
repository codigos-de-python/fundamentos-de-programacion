lista1 = []
#         0 1 2 3 4 5 6
lista2 = [2,5,7,8,6,8,8,8,5]
print(lista2)
print(lista2[4])

lista3 = [4,4.5,"Juanito"]
print(lista3)

lista3.append("Juanito el Bellako")
lista3.append("Líísóóóótó")
print(lista3)

lista4 = [3.1,2.5,1.3,1.5]
lista4.extend(lista2)
print(lista4)

lista4.sort()
print(lista4)
lista4.reverse()
print(lista4)
lista4.remove(8)
print(lista4)

lista5 = ["juan", "pedro" ,  "diego" ]

for temp in lista5:
    print(temp)
    
