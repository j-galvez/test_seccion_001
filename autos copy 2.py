'''
Cree un menu para una empresa que permita guardar autos
un auto tiene una patente, un modelo y una marca
El menu debe tener las siguientes opciones :
1.- agregar auto
2.- imprimir todos los autos
3.- buscar auto por patente
4.- eliminar auto
5.- Modificar modelo por patente
0.- salir
'''

import csv

l_auto=[]
n_auto=0


while True:

        print("")
        print("1- Agregar auto")
        print("2- Imprimir todos los autos")
        print("3- Buscar por patente")
        print("4- Eliminar auto")
        print("5- Modificar modelo por patente")
        print("6- Guardar datos")
        print("0- Salir")
        print("")

        op=int(input("Ingrese selección : "))

        if op==1:
            print("")
            print("--AGREGAR AUTO--")
            print("")
            patente=input("Ingrese patente : ")
            modelo=input("Ingrese modelo : ")
            marca=input("Ingresa marca : ")
            n_auto=n_auto+1
            d_auto={"patente":patente,
                    "modelo":modelo,
                    "marca":marca,
                    "n_auto":n_auto}
            l_auto.append(d_auto)

        elif op==2:
            print("")
            print("--AUTOS INGRESADOS--")
            for x in l_auto:
                print("")
                print("Nº DE AUTO : ", x["n_auto"])
                print("PATENTE : ", x["patente"])
                print("MODELO : ", x["modelo"])
                print("MARCA : ", x["marca"])
                print("")


        elif op==3:
            encontrado = False
            print("")
            print("--BUSCAR AUTO POR PATENTE--")
            buscar=input("Ingrese patente a buscar : ")
            for x in l_auto:
                if buscar == x["patente"]:
                    encontrado = True
                    patente=x["patente"]
                    modelo=x["modelo"]
                    marca=x["marca"]

            if encontrado:
                print("")
                print("AUTO ENCONTRADO")
                print("")
                print("PATENTE: ", patente)
                print("MODELO: ", modelo)
                print("MARCA: ", marca)

            else:
                print("AUTO NO EXISTE")

        elif op==4:
            encontrado = False
            cont_auto=0
            print("")
            print("-ELIMINAR AUTO-")
            print("")
            eliminar=input("Ingrese PATENTE de AUTO a eliminar : ")
            for x in l_auto:
                if eliminar == x["patente"]:
                    encontrado = True
                    n_auto=x["n_auto"]
                    patente=x["patente"]
                    modelo=x["modelo"]
                    marca=x["marca"]

                    l_auto.remove(x)

                    print("AUTO ELIMINADO")

                else:
                    print("PATENTE NO SE ENCUENTRA")

        elif op==5:
            encontrado=False
            print("")
            print("-MODIFICAR MODELO POR PATENTE-")
            print("")
            buscar=input("Ingrese patente : ")
            for x in l_auto:
                if buscar == x["patente"]:
                    encontrado = True
                    n_auto=x["n_auto"]
                    patente=x["patente"]
                    modelo=x["modelo"]
                    marca=x["marca"]
                    new_modelo = input("ingrese nuevo modelo : ")
                    d_auto = x["modelo"] = new_modelo

            if encontrado:
                print("--MODELO MODIFICADO--")
            else:
                print("-PATENTE NO SE ENCUENTRA-")


        elif op==6:
            with open ("datos_autos.csv", "w", newline="") as datos_autos:
                datos_autos = csv.writer(datos_autos)


                datos_autos.writerow(["n_auto", "patente", "modelo", "marca"])


                datos_autos.writerows([
                    [n_auto, patente, modelo, marca]
                ])




        elif op==0:
            print("-ADIOS-")
            break










