#Generar reaccion

#Imprimir cancion
def mostrar_ficha(cancion):
        print(cancion['titulo'] + '\n' + 
        ", ".join(cancion['artistas']) + '\n' +   
        ", ".join(cancion['generos']) + '\n' +
        cancion['album'] + '\n'+
        str(cancion['año']))   


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
