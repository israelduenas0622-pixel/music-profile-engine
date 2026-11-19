import json

#Buscar cancion o artista 
opcion_busqueda = int(input("Por favor, igresa el numeor que corresponde a lo que quieras buscar: 1.Artista, 2. Cancion o 3. Genero"))

#Cancion1
cancion = {'identificador': 'song_001', 'titulo': 'Vanish into you','artistas': ['Lady gaga'],
            'generos':['glam-rock','synth-pop','dance-pop','power-pop'],'album':'Mayhem','año':2025}

    #segunda cancion 
cancion_2 = {'identificador': 'song_002', 'titulo': 'Abracadabra','artistas': ['Lady gaga'],
            'generos':['Dance-Pop','Electro-Pop','Dark-Pop'],'album':'Mayhem','año':2025}

#Cancion3
cancion_3 = {'identificador': 'song_003', 'titulo': 'Die With a Smile','artistas': ['Lady gaga', 'Bruno Mars'],
            'generos':['Pop','Soft-Rock'],'album':'Mayhem','año':2025}

#Coleccion de canciones
biblioteca  = [cancion, cancion_2,cancion_3] 

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
        

    
    #Buscar artista
def buscar_artista (biblioteca,artista_buscado):
        canciones_encontradas = []
        for cancion in biblioteca:
            for artista in cancion['artistas']:
                artista_normalizado = artista.lower().strip()
                if artista_buscado == artista_normalizado:  
                    canciones_encontradas.append(cancion    )
        
                    
        return canciones_encontradas   

    #Buscar cancion por titulo
def buscar_cancion(biblioteca,titulo_buscado):
        for cancion in biblioteca:
            if titulo_buscado  == cancion['titulo'].lower().strip():
        
                return [cancion]
        return []

    #Buscar genero
def buscar_genero (biblioteca,genero_buscado):
        generos_encontrados = []
        for cancion in biblioteca:
            for genero in cancion['generos']:
                genero_normalizado = genero.lower().strip().replace("-", "").replace(" ","")
                if genero_buscado == genero_normalizado:
                    generos_encontrados.append(cancion)

        return generos_encontrados

#Menu
if opcion_busqueda == 1:
    artista_buscado = input('Por favor, indica el nombre del artista a buscar:').lower().strip()
    resultado_busqueda = buscar_artista(biblioteca,artista_buscado)
elif opcion_busqueda == 2:
    titulo_buscado = input('Por favor, indica el nombre de la cancion a buscar:').lower().strip()
    resultado_busqueda = buscar_cancion(biblioteca,titulo_buscado)
elif opcion_busqueda == 3:
    genero_buscado = input('Por favor, indica el nombre del genero a buscar:').lower().strip().replace("-", "").replace(" ","")
    resultado_busqueda = buscar_genero(biblioteca,genero_buscado)
else:
    print('Opcion no valida. Por favor selecciona 1,2 o 3')

#Generar reaccion
def reaccion(historial,cancion):
    reacccion_usuario = int(input("Indica que te parecio la cancion: 1. Me gusta, 2. No me gusta, 3. Necesito escucharla de nuevo, 4. Omitir"))
    if reacccion_usuario in (1,2,3):
        historial.append({'identificador': cancion['identificador'], 'reaccion': reacccion_usuario})
        


if opcion_busqueda in (1,2,3):
    if not resultado_busqueda:
        print("Canción, artista o genero no encontrado. Intenta de nuevo.")  
    else:
        for cancion in resultado_busqueda:
            mostrar_ficha(cancion)
            reaccion(historial,cancion)

guardar_historial(historial)
        

