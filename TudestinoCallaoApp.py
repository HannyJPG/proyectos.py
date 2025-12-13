import tkinter as tk 
from tkinter import messagebox
import tkintermapview 
from tkinter import*
from tkinter import ttk #---------------------enlace para el interfaz cuadro sitios populares (benjamin)-------------------------
from PIL import Image, ImageTk #----------------------para subir imagenes (benjamin) -------------------------------
import json #Es para poder utilizar datos de tipo "json" en este caso es el archivo con los nodos y aristas de todo el callao
import math #Literalmente estamos importando matematica
import networkx as nx #Sistema de analisisi y creacion de grafos
import os #Facilita la manipulacion de archivos

#instalarse el "tkintermapview" para la fucion
#Lo pueden hacer si abren la consola y escribren "pip install tkintermapview" 
#Tal como esta escrito entre comillas 
#Instalarse el "PIL" para insertar imagenes
#"pip install pillow" para instalar
#Instalar tambien lo siguiente para el funcionamiento adecuado del sistema de nodos;
#pip install osmnx networkx geopandas shapely rtree pyproj


#------------------------------------------------------------------------------------------------------
#Sistema de Nodos

def cargar_nodos(): #Esta funcion se encarga de cargar los nodos previamente descargados
    try:
        with open("callao_graph.json", "r", encoding="utf-8") as f: #Abre el archivo que contiene la informacion de los nodos
            data = json.load(f) #Lee el archivo de los nodos y lo convierte en un objeto
            return data["nodes"] #Solo regresa los nodos del archivo
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar callao_graph.json:\n{e}") #Si ocurre un error en la carga de datos lo notifica
        return {} #Si hay un error, no devulve datos, para que le programa no se rompa

NODOS_CALLAO = cargar_nodos() #Se llama a la funcion y se almacena la informacion de los nodos en la variable #NODOS_CALLAO


#Funciones de distancia 

def distancia(lat1, lon1, lat2, lon2): #Esta funcion se encarga de identificar el nodo mas cercano respecto a un punto dado
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2) #Calcula la distancia euclidiana para obtener la distancia real de los 2 puntos
                                                          #Punto A (lat1, lon1) , PuntoB (lat2,lon2)

def encontrar_nodo_mas_cercano(lat_click, lon_click):#Toma como parametros las cordenadas adquiridas al dar click al mapa
    nodo_mas_cercano = None #Variable inicializada en NONE
    min_dist = float("inf") #Se inicializa la distancia minima como infinito,  de esa manera cualquier distancia calculada, sera menor la primera vez

    for node_id, info in NODOS_CALLAO.items(): #Recorre todos los nodos cargados en NODOS_CALLAO, nodo_id es el identificador del nodo, info en un diccionario con los datos del nodo previamente cargados.
        d = distancia(lat_click, lon_click, info["lat"], info["lon"]) #Calcula la distancia entre el punto clickeado y el nodo actual usando la funcion distancia, todo se guarda en d
        if d < min_dist: #Si la distancia "d" es menor que la distancia minima (infinito)
            min_dist = d #Actualiza el valor de distancia minima
            nodo_mas_cercano = node_id #Guarda el "node_id", como el nodo mas cercano encontrado

    return nodo_mas_cercano #Devuelve el "node_id" como el nodo mas cercano encontrado


#Cargar un grafo real

def cargar_grafo_completo(): #Esta funcion se encarga de crear un grado completo con todos los nodos y aristas usando networkx
    with open("callao_graph.json", "r", encoding="utf-8") as f: #Abre el archivo de los nodos del callao en modo lectura y codificacion UTF-8
        data = json.load(f) #Convierte el contenido del archivo anterior en un diccionario de python

    G = nx.Graph() #Crea un grafo vacio usando "Networkx", el cual se llenara con los nodos y aristas del archivo anterior

    # Agregar nodos
    for node_id, info in data["nodes"].items(): #Pasa por cada nodo del diccionario
        G.add_node(node_id, lat=info["lat"], lon=info["lon"]) #Agrega el nodo al grafo junto con sus atributos "lat y lon"

    # Agregar aristas reales
    for u, lista in data["edges"].items(): #Pasa por cada arista del diccionario
        for edge in lista:
            v = edge["to"] #Destino del nodo
            dist = edge["distance"] #Distancia real entre nodos
            G.add_edge(u, v, weight=dist) #Agrega la arista al grafo con su distancia

    return G #Devuelve el grafo completo con todas las aristas y nodos cargados


GRAFO_CALLAO = cargar_grafo_completo() #Llama a la funcion y guarda el grafo completo en la variable "Grafo_Callao"
#Este nos sirve para calcular rutas mas cortas, dibujar el grafo y hacar busquedas de caminos entre nodos


#Calcular ruta

def calcular_ruta(nodoA, nodoB): #Esta funcion se encarga de buscar la ruta mas corta usando el grafo completo
    try:
        ruta = nx.shortest_path(GRAFO_CALLAO, source=nodoA, target=nodoB, weight="weight") #Usando la funcion de NetworkX se calcula la ruta mas corta entre el "nodoA" y el "nodoB"
        return ruta #Devuelve los nodos que representan la ruta mas corta
    except Exception as e: #En caso hay aun error con los nodos se notificara el error
        messagebox.showerror("Error", f"No se pudo calcular la ruta:\n{e}") #Muestra el error para saber que fallo
        return None #Si hay un erro no devuelve nada en lugar de la lista de nodos para que no se rompa
    
#Variables del sistema de calculo de ruta
puntoA = None #Nodo de inicio
puntoB = None #Nodo de destino
path_dibujado = None #Referencia a la ruta dibujada en el mapa

#Almacenamiento de rutas
ultimas_rutas = [] #Lista que almacenará las ultimas 5 rutas


#------------------------------------------------------------------------------------------------------
#VARIABLES DE LOS DATOS DE NUESTRO USUARIO PRUEBA
nombre="Juan Perez" #variables
correo="juan@gmail.com"


#(MELANY)
#Primero se crea la ventana de perfil del usuario este ira dentro de la pantalla
def ventana_de_perfil():#creamoos una ventna indepediente de perfil 
    perfil=tk.Toplevel()#ventana nueva
    perfil.title("Perfil del usuario")#establece el titulo
    perfil.geometry("350x400")#establece el tamaño
    perfil.configure(bg="#E2B379")#define el color
    perfil.resizable(False,False)#para q no se modifique el tamaño de la ventana :(
    #eitiqueta del usuario
    tk.Label(perfil,text="Datos del usuario",font=("Arial",16,"bold"),bg="#e6904b").pack(pady=10)
    tk.Label(perfil,text=f"Nombre:{nombre}",font=("Arial",12),bg="#db9696").pack(pady=5)
    tk.Label(perfil,text=f"Nombre:{correo}",font=("Arial",12),bg="#db9696").pack(pady=5)
    #historial
    historial = tk.Listbox(perfil, height=30)
    historial.pack(pady=10, padx=10, fill="both")#crea una caja tipo lista 

#David owo

    #Cargar historial de rutas guardadas
    for i, ruta in enumerate(ultimas_rutas): #Recorre cada ruta y la asigna el indice i
        historial.insert("end", f"Ruta {i+1}") #Agrega la ruta al historial "ListBox"

    #Función para mostrar ruta al seleccionarla
    def mostrar_ruta(event): #Solo se activara cuando el usuario selecione un elemento de la "ListBox" que es el historial de rutas
        seleccion = historial.curselection()  #Devuelve la informacion del elemento seleccionado en el historial
        if not seleccion: #Sirve para verificar si el usuario seleecion algo, si no, la funcion termina 
            return
        indice = seleccion[0] #Toma el primer elemento seleccionado
        ruta = ultimas_rutas[indice] #Obtiene la ruta correspondiente de la lista de rutas guardadas
        coords = [(GRAFO_CALLAO.nodes[n]["lat"], GRAFO_CALLAO.nodes[n]["lon"]) for n in ruta] #Transforma la ruta de la lista en cordenadas, para que luego se puedan dibujar en el mapa
       
        #Borrar ruta y marcadores actuales
        map_widget.delete_all_marker() #Borra todos los marcadores del mapa (los relacionados a las rutas)
        global path_dibujado #Se decllara la variable como global para usarla en otras funciones
        if path_dibujado:
            path_dibujado.delete() #Borra la tura que estaba dibujada anteriormente

        #Marcar punto A y B
        lat_a, lon_a = coords[0] #Primer nodo de la ruta
        lat_b, lon_b = coords[-1] #Ultimo nodo de la ruta
        map_widget.set_marker(lat_a, lon_a, text="A") #Se colocan los marcadores en el mapa acorde a la ruta seleccionada
        map_widget.set_marker(lat_b, lon_b, text="B") #Se colocan los marcadores en el mapa acorde a la ruta seleccionada
       
        #Dibujar ruta
        path_dibujado = map_widget.set_path(coords) #Dibuja la linea de la ruta del mapa usando las cordenadas calculadas
                                                    #Se mantiene en variable para poder borrarla despues en caso se dibuje otra ruta.

    historial.bind("<<ListboxSelect>>", mostrar_ruta) #Conecta el historial con la funcion "mostrar_ruta"


#(Benjamin)
#Ventana de los sitios populares de la ruta 
def ventana_de_sitios(): #ventana de sitios 
    escritura = StringVar() #funcion insertar texto
    punto=tk.Toplevel() #ventana nueva
    punto.title("Sitios populares") #establece el titulo
    punto.geometry("600x600") #establece el tamaño
    punto.configure(bg="#FFFFFF") #define el color
    punto.resizable(False,False)
    #Marcador de sitios
    directorio_base = os.path.dirname(os.path.abspath(__file__))
    ruta_icono = os.path.join(directorio_base, "recursos", "intpoint.png")

    try:
        icono_img = Image.open(ruta_icono)
        icono_img = icono_img.resize((22, 28)) # tamaño de la imagen pequeño (mientras mas alto el numero, mas grande)
        #el darle un tamaño al marcador es importante xq el predeterminado es demasiado grande 
        icono_marcador = ImageTk.PhotoImage(icono_img) #enlaza los terminos a uno solo
    except FileNotFoundError:
        messagebox.showerror("Error", f"No se encontró el archivo de icono:\n{ruta_icono}")
        return   
    #Agregar sitios 
    escritura1 = LabelFrame(punto, text= "Busqueda De Lugares") #inserto el titulo del primer cuadro 
    escritura1.pack(padx=20, pady=20, fill="both") #fill="both" sirve para rellenar el contorno del espacio disponible
    lbl = Label(escritura1, text="Nombre o Coordenada Del Sitio") #opcion del primer cuadro
    lbl.pack(padx=10, pady=10, side=tk.LEFT) #left = izquierdo (posicion)
    ent = Entry(escritura1, textvariable=escritura) #enlaze para insertar texto
    ent.pack(side=tk.LEFT, padx=10, pady=10)
    btn = Button(escritura1, text="Buscar", command=ventana_de_sitios) #Boton para agregar lugares de preferencia 
    #psdt: Me servira para cuando tenga la base de datos de los paraderos)
    btn.pack(side=LEFT, padx=10, pady=10)
    letra2 = LabelFrame(punto, text="Lugares Populares Del Momento") #titulo del segundo cuadro
    letra2.pack(padx=20, pady=20, fill="both") #fill="both" sirve para rellenar el contorno del espacio disponible
    tv = ttk.Treeview(letra2, columns=(1,2,3), show="headings", height=20) #Creacion de columnas y show="headings" es para mostrar nombres columnas
    tv.pack(padx=20, pady=20, fill="both") #fill="both"
    tv.heading(1, text = "Nombre") 
    tv.heading(2, text = "Actividad")
    tv.heading(3, text= "Coordenada")
    tv.column(1, width=100, anchor=CENTER) #posicion
    tv.column(2, width=100, anchor=CENTER) #posicion
    tv.column(3, width=100, anchor=CENTER) #posicion
    # Lugares predeterminado
    lugares = [
        ("Puerto del Callao", "Turismo", "-12.053926, -77.146425"),
        ("Fortaleza Real Felipe", "Turismo", "-12.0625086,-77.148792"),
        ("Museo Abtao del Callao", "Turismo", "-12.0600877, -77.1510171"),
        ("Zona Monumental del Callao", "Turismo", "-12.06007, -77.1473792"),
        ("La Caleta De La Punta", "Restaurante", "-12.074181, -77.1645797"),
        ("Cabos del Puerto Perú", "Restaurante", "-12.0602797, -77.1498709"),
        ("DONDE YOLO Restaurante", "Restaurante", "-12.0743864, -77.1647581"),
        ("El Mirador", "Restaurante", "-12.0709792, -77.1659225"),
        ("Malecón Pardo La Punta", "Recreacion", "-12.0737998, -77.165312"),
        ("Óvalo El Obelisco", "Recreacion", "-12.0515363, -77.1341431"),
        ("Playa Malecon Pardo", "Recreacion", "-12.0697962, -77.1639625"),
        ("Playa La Arenilla", "Recreacion", "-12.0726425, -77.1593012"),
    ]

    for lugar in lugares: #usamos "lugar" sea asignado como "lugares" y "lugares" para que recorra la lista predeterminada
        nombre = lugar[0] #lugar [0] para acceder a primera elemnto en una secuencia 
        parte1, parte2 = map(float, lugar[2].split(",")) #parte1 y parte2 seran numeros 
        #.split(",") es el metodo para divir la cadena (coordenadas) con la ","
        map_widget.set_marker(parte1, parte2, text=nombre, icon=icono_marcador) #Aqui se vincula el marcador con la imagen 
        tv.insert("", "end", values=lugar) #Me permite insertar los datos en la ventana y "values= lugar" es par acontener los valores
    
    def ir_a_lugar(evento): #nos servira para que con un doble click en la tabla vaya al marcador 
        #el termino "evento", a pesar de no estar activo, tiene una funcion interna que se activa una vez que el programa esta activo 
        #Nos permite que "ir_a_lugar" reciba al informacion del doble click 
        #Se le llama "estructura Binding" (para mas info chequeen material complementario)
        item = tv.selection() #aqui seleccionados la fila correspondiente 
        if not item: #en caso de contrario 
            return

        valores = tv.item(item, "values") #carga los valores de la fila de la tabla 
        lat, lon = map(float, valores[2].split(",")) #separa las coordenadas y las vuelve numeros 

        map_widget.set_position(lat, lon) #mueve en el mapa al lugar seleccionado 
        map_widget.set_zoom(17) #tamaño del mapa a la hora de sleccionar la busqueda

    tv.bind("<Double-1>", ir_a_lugar) #"<Double-1>" es para conectar "evento" con el doble click

#FUNCIONALIDAD DEL LOGIN.............................
usuario="admin"
contraseña="1234"#para ingresar al sistema
def usuario_login():
    usuario = entry1.get()#obtiene el texto de la entrada
    clave = entry2.get()#obtiene en la caja de la clave

    if usuario == "admin" and clave == "1234": #con este bucle se valida el usuario y la clave 
        messagebox.showinfo("Éxito", "Su sesión fue correcta")
        ventana_login.destroy()
        abrir_ventana_principal()  #cierra la ventana de login 
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")#en caso de error muestra este mensaje

ventana_login = tk.Tk() 
ventana_login.geometry("400x250")#tamaño de la ventana
ventana_login.title("👤      Inicio de sesión")#se le coloco un icono nose como se coloca lo inetente DX
ventana_login.configure(bg="#ffcc99")#color de la ventana
#fomdo del login

# Etiquetas
tk.Label(ventana_login,text="NOMBRE",bg="#ffffff").place(x=20,y=50)
tk.Label(ventana_login,text="PASSWORD",bg="#ffffff").place(x=20,y=100)
#Entradas de texto 
entry1=tk.Entry(ventana_login,bg="black",fg="white",borderwidth=5  )
entry1.place(x=100,y=50,width=250,height=30)
entry2=tk.Entry(ventana_login,show="*",bg="black",fg="white",borderwidth=5)
entry2.place(x=100,y=100,width=250,height=30)
#Boton del login
tk.Button(ventana_login,text="Iniciar secion",command=usuario_login).place(x=150,y=150)


#ventana porincipal en el que esta el mapa uwu
def abrir_ventana_principal():#se creo una funcion para abrir la ventana principal
    global ventana #se declara la variable global para usarla en otras funciones
    ventana = tk.Tk()
    ventana.geometry("1020x680") #tamaño de la ventana
    ventana.title("TuDestino,LimaApp") #nombre de la ventana
    ventana.resizable(True, True) #para modificar la ventana a gusto 
#panel de la izquierda
    frame_izq=tk.Frame(ventana,width=500,bg="#c58817") #color del panel
    frame_izq.pack(side="left",fill="y") #posicion del panel
#boton el cual nos dara acceso al perfil
    tk.Button(frame_izq,text="👤 Mi perfil",width=15,height=2,command=ventana_de_perfil).pack(pady=20)
#Boton para sitios calientes
    tk.Button(frame_izq,text="★ Hot Places",width=15,height=2,command=ventana_de_sitios).pack(pady=20)

#MAPA 
    frame_mapa = tk.Frame(ventana, width=700, height=400)
    frame_mapa.place(x=350, y=0)  # posición dentro de la ventana
    #---------------------------------------------------------------------------------------------
    global map_widget #CORRECION A CONVENIENCIA (POR PARTE DE BENJAMIN/NOS SIRVE PARA MANIPULAR DATOS MAPAS DE MANERA INTERACIVA)
    #------------------------------------------------------------------------------------------
    map_widget = tkintermapview.TkinterMapView(frame_mapa, width=600, height=680, corner_radius=0) #tamaño de la ventana
    map_widget.pack(fill="both", expand= True) #para permitir el zoom

    map_widget.set_position(-12.0625086,-77.148792)  #coordenadas del cercado de lima (Centro del distrito de Lima)
    map_widget.set_zoom(17) #mientras en numero más alto = mayor zoom


  #Interaccion con el mapa mediante clicks

    def click_en_mapa(coordenadas): #Esta funcion se encarga de almacenar las cordenadas del lugar al cual se hizo click en el mapa
        global puntoA, puntoB, path_dibujado #Se declara estas variables como globables, es decir, se usaran y modificaran al inicio del programa

        lat, lon = coordenadas #Se divide las crdenadas en 2 varibles distintas para obtener la latitud y longitud por separado

        # Seleccionar punto A
        if puntoA is None:
            puntoA = encontrar_nodo_mas_cercano(lat, lon) #Busca el nodo mas cercano a las cordenadas clickeadas
            map_widget.set_marker(lat, lon, text="A") #Coloca un marcador en donde se clickeo
            print("Punto A asignado:", puntoA) #Muestra en la consola el nodo asignado y sus cordenadas

        # Seleccionar punto B
        elif puntoB is None:
            puntoB = encontrar_nodo_mas_cercano(lat, lon) #Busca el nodo mas cercano al click
            map_widget.set_marker(lat, lon, text="B") #Coloca un marcador donde se clickeo
            print("Punto B asignado:", puntoB) #Nuestra en la consola el nodo asignado y sus cordenadas

            # Calcular ruta real
            ruta = calcular_ruta(puntoA, puntoB) #Usando la funcion "calcular_ruta", devuelve una lista de los nodos que forman la ruta mas corta

            if ruta:
                coords = [(GRAFO_CALLAO.nodes[n]["lat"], GRAFO_CALLAO.nodes[n]["lon"]) for n in ruta] #Si existe una ruta, convierte las cordenadas de latitud y longitud para poder diburlas en el mapa

                # Dibujar línea de la ruta
                path_dibujado = map_widget.set_path(coords) #Dibuja la ruta en el mapa
                print("Ruta generada con", len(coords), "puntos.") #Muestra en la consola cuantos puntos tiene la ruta

                #Guardar ruta en historial
                if len(ultimas_rutas) >= 5: #Si ya hay 5 rutas, eliminamos la primera para mantener solo las últimas 5
                    ultimas_rutas.pop(0) #Elimina el primer elemento de la lista (la ruta mas antigua)
                ultimas_rutas.append(ruta) #Agrega la ruta recien calculada al final del historial de rutas

        # Reiniciar todo con el tercer clic
        else:
            puntoA = None #Se reinicia el valor
            puntoB = None #Se reinicia el valor
            map_widget.delete_all_marker() #Si hay un tercer click, se borran todos los marcadores del mapa
            if path_dibujado:
                path_dibujado.delete() #Borra la ruta dibujada
            print("Selección reiniciada. Elige A y B nuevamente.")

    # Activar clic
    map_widget.add_left_click_map_command(click_en_mapa) #Vincula la funcion "Click en mapa", al click izquierdo

#Limitaciones del mapa para que solo se pueda desplazar por lima owo
    min_lat=-12.40 #Limite sur   (latitud)
    max_lat=-11.70 #Limite norte (latitud)
    min_lon=-77.20 #Limite oeste (longitud)
    max_lon=-76.80 #Limite este  (longitud)

    def limitar_mov_mapa():  #funcion para limitar el desplazamiento del mapa
        lat,lon=map_widget.get_position() #obtenemos la posicion real del mapa (cuando nos desplazamos)
        nueva_lat = lat   #Copias de la posicion actual (latidud y longitud), las cuales usamos para corrgeir la posicion
        nueva_lon = lon

    # Corregir latitud (las copias guardadas)
        if lat < min_lat:         #Verifica si la latidud actual esta por debajo del limite minimo 
            nueva_lat = min_lat   #Corrige su posicion 
        elif lat > max_lat:       #Verifica si la latidud actual esta por encima del limite maximo
            nueva_lat = max_lat   #Corrige la posicion 

    # Corregir longitud (las copias guardadas)
        if lon < min_lon:         #Verifica si la longitud actual es por debajo del limite minimo
            nueva_lon = min_lon   #Corrige la posicion
        elif lon > max_lon:       #Verifica si la longitud actual esta por encima del limite maximo
            nueva_lon = max_lon   #Corrige la posicion
   
        if nueva_lat != lat or nueva_lon != lon:          #Verifica si las copias son diferentes a las originales
            map_widget.set_position(nueva_lat, nueva_lon) #Actualiza las originales acorde a la posicion de las copias

        ventana.after(80, limitar_mov_mapa) #Se encarga de ejecutar la funcion de "limitar_mov_map" cada 80ms, con el fin de corregir la posicion  de manera constante
                                            
    limitar_mov_mapa()  #Llama a la funcion por primera vez, luego se mantiene activa gracias al "ventana.after"

    ventana.mainloop()
ventana_login.mainloop() #buble que mantiene el tkinter
