# Archivo con la logica principal del proyecto.
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def cargar_y_copiar_imagenes():
    
    copias = []
    path= "./images"
    archivos = [f for f in os.listdir(path) if f.endswith('.jpg')]

    # Leer la imagen en formato BGR
    for i, archivo in enumerate(archivos):
        ruta_imagen = os.path.join(path, archivo)
        imagen = cv2.imread(ruta_imagen)

        # Verificar si la imagen se ha cargado correctamente
        if imagen is not None:
            imagen_copy = imagen.copy()

            # Convertir la imagen a RGB
            imagen_rgb = cv2.cvtColor(imagen_copy, cv2.COLOR_BGR2RGB)

            # Añadir la imagen convertida a la lista
            copias.append(imagen_rgb)
        else:
            print(f"Error al cargar la imagen: {ruta_imagen}")

    return copias


copias= cargar_y_copiar_imagenes()

print(len(copias))
