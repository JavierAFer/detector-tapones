import cv2
import numpy as np
import imutils
import os
import matplotlib.pyplot as plt


class GestorImagenes:
    def __init__(self, directorio="./images"):
        self.directorio = directorio

    def cargar_y_copiar_imagenes(self):
        copias = []
        
        # Verificar si el directorio existe
        if not os.path.exists(self.directorio):
            print(f"El directorio {self.directorio} no existe.")
            return copias
        
        # Obtener lista de archivos .jpg
        archivos = [f for f in os.listdir(self.directorio) if f.endswith('.jpg')]

        # Leer las imágenes en formato BGR, copiar y convertir a RGB
        for archivo in archivos:
            ruta_imagen = os.path.join(self.directorio, archivo)
            imagen = cv2.imread(ruta_imagen)

            if imagen is not None:
                imagen_copy = imagen.copy()
                copias.append(imagen_copy)
            else:
                print(f"Error al cargar la imagen: {ruta_imagen}")

        return copias
    

