import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import imutils


def cargar_y_copiar_imagenes():
    copias = []
    path = "./images"  # Asegúrate de que este directorio exista
    archivos = [f for f in os.listdir(path) if f.endswith('.jpg')]

    # Leer la imagen en formato BGR
    for archivo in archivos:
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

# Función para mostrar los valores HSV al pasar el cursor
def mostrar_valores_hsv(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        # Obtener el valor HSV del pixel en las coordenadas (x, y)
        h, s, v = imagen_hsv[y, x]

        # Crear una copia de la imagen original para mostrar el texto
        imagen_mostrada = imagen.copy()

        # Añadir el texto con los valores HSV a la imagen
        texto = f'H: {h}, S: {s}, V: {v}'
        cv2.putText(imagen_mostrada, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Mostrar la imagen con el texto
        cv2.imshow('Imagen HSV', imagen_mostrada)

# Cargar las imágenes
copias = cargar_y_copiar_imagenes()

# Verificar si se cargaron imágenes
if len(copias) == 0:
    print("No se encontraron imágenes en el directorio.")
else:
    # Elegir la primera imagen para trabajar
    imagen = copias[7]  # Puedes modificar esto para seleccionar otra imagen
    # Convertir a HSV
    imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_RGB2HSV)

    # Mostrar la imagen original y permitir la interacción
    cv2.imshow('Imagen HSV', imagen)
    cv2.setMouseCallback('Imagen HSV', mostrar_valores_hsv)

    # Esperar hasta que se presione una tecla
    cv2.waitKey(0)
    cv2.destroyAllWindows()