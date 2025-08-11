#Programa de piedra ,papel o tijera 
def piedra_papel_tijera():
    import random
    opciones=["piedra","papel","tijera"]
    jugador = input("Elije una opcion  : piedra , papelo tijera: ").lower()
    computadora = random.choice(opciones)
    print(f"jugador: {jugador} - computadora:{computadora}")
    if jugador == computadora:
        print("Empate")
    elif(jugador=="piedra"and computadora=="tijera")or\
        (jugador=="papel"and computadora=="piedra ")or\
        (jugador=="tijera"and computadora=="papel "):
        print("Ganaste")
    else :
        print("Perdiste")
piedra_papel_tijera()

        