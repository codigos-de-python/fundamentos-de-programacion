def agregarAnimal():
    

opcion =0
listaAnimales=[]
hora=[]
diccionario={}
while opcion!=6:
    try:
        print("Veterinaria Cucho")
        print("1-Agregar mascota ")
        print("2-Listar Mascotas")
        print("3-Eliminar Mascotas")
        print("4-Buscar Mascotas")
        print("5-Agendar hora")
        print("6-Salir")
        opcion = int(input("Seleccione opcion"))
    except:
        print("Ingrese la opcion correcta")
    
    if opcion==1:
        agregarAnimal()
    elif opcion==2:
        listarAnimales()
    elif opcion==3:
        eliminarMascota()
    elif opcion==4:
        buscarMascota()
    elif opcion==5:
        agendarHora()
    elif opcion==6:
        print("Adios")
    else:
        print("Ingrese opcion correcta")