def crear_contraseñas(num):
    chr="abcdefghijk    "
    num_entero = str(num)
    num =int(num_entero[0])
    c1=  num+2
    c2=num
    c3=num-5
    contraseña = f"{chr[c1]}{chr[c2]}{chr[c3]}{num*2}"
    print("Tu  nueva contraseña es ,",contraseña)
crear_contraseñas(5)
    