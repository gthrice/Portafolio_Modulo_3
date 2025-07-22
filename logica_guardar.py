RUTA_ARCHIVO = "inventario.json" 

import os
import json

def cargar_objeto():
    if not os.path.exists(RUTA_ARCHIVO):
        return []
    try:
        with open(RUTA_ARCHIVO, "r", encoding='utf-8') as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []

def guardar_objeto(tareas):
    with open(RUTA_ARCHIVO, "w", encoding='utf-8') as archivo:
        json.dump(tareas, archivo)