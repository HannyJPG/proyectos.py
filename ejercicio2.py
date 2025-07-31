 Hola falta la funcionalidad :P
#DEfinimos una funcion llamada operaxiones
def operaciones():
    print("Bienvenido Menu de operaciones ")
    print("1 : Sumar")
    print("2: Restar")
    print("3 : Multiplicar")
    print("4 : Dividir ")
    print("5 : Salir ")
    
#Usaremos la funcion do while para las operaciones 
while True :  
    operaciones()
    opcion=input("Elija una opcion del 1 al 5: ")
    if opcion =="5":
        print(" Adios , muchas gracias uwu")
        
#Palabra reservada try q se usa para ejecutar un bloque q puede causar error
    try:
        n1 = float("Ingrese primer numero") -> pinshi error tmreeeeeeee
        n2= float("Ingrese asegundo numero")
        if opcion =="1":
            resultado = n1+n2
            print(f"El resultado de la suma es {resultado}")
        elif opcion =="2":
            resultado = n1-n2
            print(f"El resultado de la resta es {resultado}")
        elif opcion =="3":
            resultado = n1*n2
            print(f"El resultado de la resta es {resultado}")
        elif opcion =="4":
            if n2!=0:
                resultado = n1/n2
                print(f"El resultado de la resta es {resultado}")
            else :
                print("no es divisible por cero")
        else :
            print("Ingrese un numero valido")   
    except ValueError:
        print("no es popsible el dato estra incorrecto")
    print("-------------------Gracias-------------------------")
