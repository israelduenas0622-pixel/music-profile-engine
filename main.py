import json
from busquedas import buscar_artista, buscar_cancion, buscar_genero,normalizar_genero
from historial import guardar_historial, cargar_historial


#Cancion1
cancion = {'identificador': 'song_001', 'titulo': 'Vanish into you','artistas': ['Lady gaga'],
            'generos':['Glam-rock','synth-pop','dance-pop','power-pop'],'album':'Mayhem','año':2025}

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

historial = cargar_historial()

#Coleccion de canciones
biblioteca  = [cancion, cancion_2,cancion_3, cancion_4] 

puntaje_reaccion = {1:1,2:-1,3:0.5,4:0}


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
                    genero = normalizar_genero(genero)
                    if genero not in generos_favoritos:
                        generos_favoritos[genero] = puntaje
                    else:
                        generos_favoritos[genero] += puntaje
    return generos_favoritos

def visualizar_perfil_generos(generos_favoritos):
    print("Generos favoritos:")
    for genero, puntaje in sorted(generos_favoritos.items(), key=lambda x: x[1], reverse=True):
        print(f"- {genero}: {puntaje}")

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
        

