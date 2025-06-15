import random

suerte = []
print("")
print("Ingrese sus 7 números de la suerte")
for numero in range(7):
    suerte.append(int(input("Ingrese su número: "))) #linea 1

print("")
print("Usted ingresó los siguientes números:", suerte)

for ronda in range(3):
    lista = []
    for turno in range(1, 7 + 1):
        flag = True
        while flag:
            aleatorio = random.randint(1, 49)
            if lista.count(aleatorio) == 0:
                lista.append(aleatorio)
                flag = False

print("")
print("")
print(f"Los números sorteados en la ronda {ronda + 1} fueron:")

for numero in lista:
    print(numero)# Línea incógnita 4
    print("")

contador = 0
for numero in suerte:
    if lista.count(numero) == 1:
        contador += 1

if contador == 7:
    print("¡Hoy es su día de suerte. Ha ganado!")
    for i in range(10):
        print("¡¡¡¡¡¡Eres un ganador!!!!!!!!!!")
        break
else:
    print("Lo siento, pero no has ganado en esta ronda")