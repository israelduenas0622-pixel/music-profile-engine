import json

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


#Reiniciar historial
def reiniciar_historial(historial):
    historial.clear()
    guardar_historial(historial)

