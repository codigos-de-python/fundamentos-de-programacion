mayornum = -1
menornum = 101

while True:

    print("*** Menu Principal***")
    print("1-Ingresar Numero")
    print("2-Mostrar Mayor")
    print("3-Mostar Menor")
    print("4-Salir")

    try:
        opcion = int(input("Elija una opcion: "))
    except ValueError:
        print("Ingrese un valor numerico")
    
    if opcion == 1:
        while True:
            try:
                num_ingresado = int(input("Ingrese un número entre 0 y 100: "))
                if num_ingresado >=0 and num_ingresado <=100:
                    print("Ingreso Exitoso")
                    num_ingresado
                    if num_ingresado > mayornum:
                        mayornum = num_ingresado
                    if num_ingresado < menornum:
                        menornum = num_ingresado
                    break
                else:
                    print("Debe ingresar un numero entre 0 y 100")   
            except:
                print("Debe ingresar un numero entero")
                continue

    elif opcion ==2:
        if mayornum == -1:
            print("No sean ingresado numeros")
        else:
            print(f"El numero mayor hasta el momento es {mayornum}")
    
    elif opcion ==3:
        if mayornum == 101:
            print("No sean ingresado numeros")
        else:
            print(f"El numero menor hasta el momento es {menornum}")
    
    elif opcion ==4:
        print("Fin del programa, Adios")
        break

    else:
        print("Ingrese una opcion valida")
