#Biblioteca de canciones
cancion = {'titulo': 'Vanish into you','artistas': ['lady gaga'],
        'generos':['glam-rock','synth-pop','dance-pop','power-pop'],'album':'mayhem','año':2025}

#segunda cancion 
cancion_2 = {'titulo': 'Abracadabra','artistas': ['lady gaga'],
        'generos':['Dance-Pop','Electro-Pop','Dark-Pop'],'album':'mayhem','año':2025}

biblioteca  = [cancion, cancion_2]

#Imprimir cancion
def mostrar_ficha(cancion):
    print(cancion['titulo'] + '\n' +
    ", ".join(cancion['artistas']) + '\n' +
    ", ".join(cancion['generos']) + '\n' +
    cancion['album'] + '\n'+
    str(cancion['año']))    

for cancion in biblioteca:
    mostrar_ficha(cancion)