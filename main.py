import json


#Cancion1
cancion = {'identificador': 'song_001', 'titulo': 'Vanish into you','artistas': ['Lady gaga'],
            'generos':['glam-rock','synth-pop','dance-pop','power-pop'],'album':'Mayhem','año':2025}

    #segunda cancion 
cancion_2 = {'identificador': 'song_002', 'titulo': 'Abracadabra','artistas': ['Lady gaga'],
            'generos':['Dance-Pop','Electro-Pop','Dark-Pop'],'album':'Mayhem','año':2025}

#Cancion3
cancion_3 = {'identificador': 'song_003', 'titulo': 'Die With a Smile','artistas': ['Lady gaga', 'Bruno Mars'],
            'generos':['Pop','Soft-Rock'],'album':'Mayhem','año':2025}

cancion_4 = {
    'identificador': 'song_004',
    'titulo': 'Vogue',
    'artistas': ['Madonna'],
    'generos': ['Dance-Pop', 'House'],
    'album': 'I’m Breathless',
    'año': 1990
}


#Coleccion de canciones
biblioteca  = [cancion, cancion_2,cancion_3, cancion_4] 

puntaje_reaccion = {1:1,2:-1,3:0.5,4:0}


#Funciones historial
def guardar_historial(historial):
    with open('historial.json', 'w') as archivo_historial:
        json.dump(historial, archivo_historial)


def cargar_historial():
    try:
        with open('historial.json', 'r') as archivo_historial:
            historial = json.load(archivo_historial)
    except FileNotFoundError:
        historial = []
    return historial

historial = cargar_historial()

    #Imprimir cancion
def mostrar_ficha(cancion):
        print(cancion['titulo'] + '\n' + 
        ", ".join(cancion['artistas']) + '\n' +   
        ", ".join(cancion['generos']) + '\n' +
        cancion['album'] + '\n'+
        str(cancion['año']))   

def perfil_generos(historial,biblioteca):
    generos_favoritos = {}
    for reaccion in historial:
        puntaje = puntaje_reaccion[reaccion['reaccion']]
        for cancion in biblioteca:
            if cancion['identificador'] == reaccion['identificador']:
                for genero in cancion['generos']:
                    if genero not in generos_favoritos:
                        generos_favoritos[genero] = puntaje
                    else:
                        generos_favoritos[genero] += puntaje
    return generos_favoritos

def visualizar_perfil_generos(generos_favoritos):
    print("Generos favoritos:")
    for genero, puntaje in sorted(generos_favoritos.items(), key=lambda x: x[1], reverse=True):
        print(f"- {genero}: {puntaje}")

def normalizar_texto(texto):
    return texto.lower().strip()

def normalizar_genero(genero):
    return normalizar_texto(genero).replace("-", "").replace(" ","")


    #Buscar artista
def buscar_artista (biblioteca,artista_buscado):
        canciones_encontradas = []
        artista_buscado = normalizar_texto(artista_buscado)
        for cancion in biblioteca:
            for artista in cancion['artistas']:
                artista_normalizado = normalizar_texto(artista)
                if artista_buscado in artista_normalizado:  
                    canciones_encontradas.append(cancion)
        
        return canciones_encontradas   

    #Buscar cancion por titulo
def buscar_cancion(biblioteca,titulo_buscado):
        titulo_buscado = normalizar_texto(titulo_buscado)
        canciones_encontradas = []
        for cancion in biblioteca:
            titulo_normalizado = normalizar_texto(cancion['titulo'])
            if titulo_buscado in titulo_normalizado:
                canciones_encontradas.append(cancion)
        
        return canciones_encontradas

    #Buscar genero
def buscar_genero (biblioteca,genero_buscado):
        generos_encontrados = []
        genero_buscado = normalizar_genero(genero_buscado)
        for cancion in biblioteca:
            for genero in cancion['generos']:
                genero_normalizado = normalizar_genero(genero)
                if genero_buscado in genero_normalizado:
                    generos_encontrados.append(cancion)
                    break  # Salir del bucle de géneros si se encuentra una coincidencia

        return generos_encontrados

#Generar reaccion
def reaccion(historial,cancion):
    while True:
        try:
            reacccion_usuario = int(input("Indica que te parecio la cancion: 1. Me gusta, 2. No me gusta, 3. Necesito escucharla de nuevo, 4. Omitir"))

        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if reacccion_usuario in (1,2,3,4):
            historial.append({'identificador': cancion['identificador'], 'reaccion': reacccion_usuario})
            print("Reacción registrada.")
            break
        else:
            print("Opción inválida. Por favor, selecciona entre las opciones válidas: 1, 2, 3 o 4.")
        
def procesar_resultados(resultado_busqueda,historial):
    if not resultado_busqueda:
        print("Canción, artista o genero no encontrado. Intenta de nuevo.")  
    else:
        for i, cancion in enumerate(resultado_busqueda):
            print(f"\nCanción {i +1 }: {cancion['titulo']} - {", ".join(cancion['artistas'])}")
        while True:
            try:
                cancion_seleccionada = int(input("Por favor, indica el numero de la cancion que quieres escuchar: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue
            if cancion_seleccionada < 1 or cancion_seleccionada > len(resultado_busqueda):
                print("Número de canción inválido. Intenta de nuevo.")
            else:
                cancion = resultado_busqueda[cancion_seleccionada - 1]
                mostrar_ficha(cancion)
                reaccion(historial,cancion)
                break


#Loop menu  
while True:
    try:
        opcion_busqueda = int(input("Por favor, igresa el numero que corresponde a lo que quieras buscar: " \
"1.Artista, 2. Cancion, 3. Genero ,4.Ver perfil de generos, 5. Salir"))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue    
    if opcion_busqueda == 1:
        artista_buscado = input('Por favor, indica el nombre del artista a buscar:')
        resultado_busqueda = buscar_artista(biblioteca,artista_buscado)
    elif opcion_busqueda == 2:
        titulo_buscado = input('Por favor, indica el nombre de la cancion a buscar:')
        resultado_busqueda = buscar_cancion(biblioteca,titulo_buscado)
    elif opcion_busqueda == 3:
        genero_buscado = input('Por favor, indica el nombre del genero a buscar:')
        resultado_busqueda = buscar_genero(biblioteca,genero_buscado)
    elif opcion_busqueda == 4:
        generos_favoritos = perfil_generos(historial,biblioteca)
        visualizar_perfil_generos(generos_favoritos)
    elif opcion_busqueda == 5:
        print("Gracias por usar la aplicación. ¡Hasta luego!")
        break
    else:
        print('Opcion no valida. Por favor selecciona entre las opciones validas: 1, 2, 3 o 4.')

    if opcion_busqueda in (1, 2, 3):
        procesar_resultados(resultado_busqueda,historial)  




guardar_historial(historial)
        

