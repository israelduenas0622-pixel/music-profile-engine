from main import normalizar_genero
puntaje_reaccion = {1:1,2:-1,3:0.5,4:0}

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
