#menu de opciones con su precio
#elegir añadir al carrito y su cantidad: guardar la compra temporalmente ,
#ver el total de mi compra : retroceder 
#cuando se decida ;un resumen final : finalizar la compra
def mostrar_menu():
    print("\nBienvenido a la panadería Kitty")
    print("1. Galletas chocochips - S/. 3.00")
    print("2. Keke de vainilla   - S/. 5.00")
    print("3. Alfajores          - S/. 5.00")
    print("4. Empanadas de pollo - S/. 4.50")
    print("5. Finalizar compra")
    print("6. Ver mi carrito")


def carrito():
    carrito_compras = []
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción que desea: ")

        if opcion == "1":
            cantidad = int(input("Cantidad de galletas: "))
            carrito_compras.append(("Galletas chocochips", cantidad, 3.00 * cantidad))
        elif opcion == "2":
            cantidad = int(input("Cantidad de kekes: "))
            carrito_compras.append(("Keke de vainilla", cantidad, 5.00 * cantidad))
        elif opcion == "3":
            cantidad = int(input("Cantidad de alfajores: "))
            carrito_compras.append(("Alfajores", cantidad, 5.00 * cantidad))
        elif opcion == "4":
            cantidad = int(input("Cantidad de empanadas: "))
            carrito_compras.append(("Empanadas de pollo", cantidad, 4.50 * cantidad))
        elif opcion == "5": 
            if carrito_compras:
                print("\nResumen de compra:")
                total = 0
                for item in carrito_compras:
                    print(f"{item[0]} - Cantidad: {item[1]}, Subtotal: S/.{item[2]:.2f}")
                    total += item[2]
                print(f"TOTAL A PAGAR: S/.{total:.2f}")
            else:
                print("\nNo compraste nada. ¡Hasta la próxima!")
            break
        elif opcion == "6":  # Ver carrito
            if not carrito_compras:
                print("\nEl carrito está vacío.")
            else:
                print("\nContenido del carrito:")
                total = 0
                for item in carrito_compras:
                    print(f"{item[0]} - Cantidad: {item[1]}, Subtotal: S/.{item[2]:.2f}")
                    total += item[2]
                print(f"Total parcial: S/.{total:.2f}")
        else:
            print("Opción no válida. Intente nuevamente.")



carrito()