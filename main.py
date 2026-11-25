import json
from busquedas import buscar_artista, buscar_cancion, buscar_genero,normalizar_genero
from historial import guardar_historial, cargar_historial, reiniciar_historial
from perfil import perfil_generos, visualizar_perfil_generos
from interfaz import mostrar_ficha, reaccion, procesar_resultados


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


#Loop menu  
while True:
    try:
        opcion_busqueda = int(input("Por favor, selecciona una opción: " \
"1.Artista, 2. Cancion, 3. Genero ,4.Ver perfil de generos, 5. Reiniciar historial, 6. Salir"))
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
        confirmacion = input("¿Estás seguro de que deseas reiniciar el historial? (s/n): ")
        confirmacion = confirmacion.lower().strip()
        while confirmacion not in ['s', 'n']:   
            confirmacion = input("Opción no válida. Por favor, ingresa 's' para sí o 'n' para no: ")
            confirmacion = confirmacion.lower().strip()
        if confirmacion == 's':
            reiniciar_historial(historial)
            print("Historial reiniciado.")
        elif confirmacion == 'n':
            print("Reinicio de historial cancelado.")
    elif opcion_busqueda == 6:
        print("Gracias por usar la aplicación. ¡Hasta luego!")
        break
    else:
        print('Opcion no valida. Por favor selecciona entre las opciones validas.')

    if opcion_busqueda in (1, 2, 3):
        procesar_resultados(resultado_busqueda,historial)  




guardar_historial(historial)
        

