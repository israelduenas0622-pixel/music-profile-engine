

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
