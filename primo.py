# Pedir cantidad de números a verificar
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de números a verificar: "))
        break
    except ValueError:
        print("Debe ingresar un número entero.")

primos = 0
no_primos = 0
contador = 0  


while contador < cantidad:
    # Solicitar número y validar que sea entero
    while True:
        try:
            numero = int(input("Ingrese número: "))
            break
        except ValueError:
            print("Debe ingresar un número entero.")

    # Verificar si el número es primo
    if numero < 2:
        es_primo = False
    else:
        es_primo = True
        divisor = 2        
        while divisor < numero:
            if numero % divisor == 0:
                es_primo = False
                break
            divisor = divisor +1

    # Mostrar resultado
    if es_primo:
        print("tu numero es primo.")
        primos = primos +1
    else:
        print("tu nuemero no es primo.")
        no_primos = no_primos +1

    contador = contador +1  

# Mostrar resumen final
print(f"Se ingresaron {primos} números primos.")
print(f"Se ingresaron {no_primos} números no primos.")