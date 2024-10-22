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
    

class GestorMascaras:
    def __init__(self, imagen):
        self.imagen = imagen
        self.imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

        # Definición de los límites de los colores en HSV
        self.colores = {
            "negro": ([90, 30, 10], [130, 120, 80]),
            "blanco": ([96, 15, 170], [145, 35, 250]),
            "azul claro": ([102, 95, 145], [108, 165, 220]),
            "azul": ([113, 170, 70], [120, 240, 150]),
            "rojo1": ([0, 130, 80], [30, 235, 190]),  # Parte 1 de rojo
            "rojo_2": ([178, 130, 80], [180, 240, 210]),  # Parte 2 de rojo
            "rosa fuerte": ([170, 130, 80], [177, 240, 210]),
            "rosa claro": ([140, 7, 140], [175, 60, 230])
        }

    def crear_mascara(self, color):
        """Crea una máscara para un color específico"""
        if color == "rojo":
            # Caso especial del azul, ya que tiene dos rangos
            lower1, upper1 = self.colores["rojo1"]
            lower2, upper2 = self.colores["rojo_2"]
            mask1 = cv2.inRange(self.imagen_hsv, np.array(lower1), np.array(upper1))
            mask2 = cv2.inRange(self.imagen_hsv, np.array(lower2), np.array(upper2))
            return cv2.add(mask1, mask2)
        elif color in self.colores:
            lower, upper = self.colores[color]
            return cv2.inRange(self.imagen_hsv, np.array(lower), np.array(upper))
        else:
            print(f"Color {color} no reconocido.")
            return None
