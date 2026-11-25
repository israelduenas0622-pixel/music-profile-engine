import json

def cargar_biblioteca():
    try:
        with open('biblioteca.json', 'r') as archivo_biblioteca:
            biblioteca = json.load(archivo_biblioteca)
    except FileNotFoundError:
        biblioteca = []
    return biblioteca