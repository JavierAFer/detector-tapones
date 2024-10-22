from clases import GestorImagenes, GestorMascaras
import cv2

def mostrar_menu_colores():
    """Mostrar la lista de colores disponibles para elegir"""
    colores_disponibles = [
        "negro", 
        "blanco", 
        "azul claro", 
        "rojo", 
        "azul", 
        "rosa claro", 
        "rosa fuerte"
    ]
    
    print("Colores disponibles:")
    for idx, color in enumerate(colores_disponibles, 1):
        print(f"{idx}. {color}")
    
    return colores_disponibles

def main():
    # Mostrar menú de colores disponibles
    colores_disponibles = mostrar_menu_colores()
    
    # Pedir al usuario que elija uno o varios colores
    color_elegido = input("Introduce los colores que deseas (separados por comas): ").lower()
    
    # Separar los colores por comas y eliminar espacios en blanco extra
    colores_seleccionados = [color.strip() for color in color_elegido.split(',')]
    
    # Comprobar si el usuario seleccionó "mascara completa"
    if "mascara completa" in colores_seleccionados:
        # Cargar una imagen desde el directorio
        gestor_imagenes = GestorImagenes("./images")
        imagenes = gestor_imagenes.cargar_y_copiar_imagenes()

        if not imagenes:
            print("No se encontraron imágenes.")
            return

        # Seleccionar la primera imagen para procesar
        imagen = imagenes[0]

        # Crear un gestor de máscaras
        gestor_mascaras = GestorMascaras(imagen)

        # Combinar todas las máscaras
        mascara_completa = gestor_mascaras.combinar_mascaras(colores_disponibles)
        gestor_mascaras.dibujar_contornos(mascara_completa, min_area=8000, max_area=20000000)
    else:
        # Validar si los colores seleccionados son válidos
        for color in colores_seleccionados:
            if color not in colores_disponibles:
                print(f"El color '{color}' no es válido. Por favor, selecciona colores válidos.")
                return

        # Cargar una imagen desde el directorio
        gestor_imagenes = GestorImagenes("./images")
        imagenes = gestor_imagenes.cargar_y_copiar_imagenes()

        if not imagenes:
            print("No se encontraron imágenes.")
            return

        # Seleccionar la primera imagen para procesar
        imagen = imagenes[0]

        # Crear un gestor de máscaras
        gestor_mascaras = GestorMascaras(imagen)

        # Combinar las máscaras para los colores seleccionados
        mascara_combinada = gestor_mascaras.combinar_mascaras(colores_seleccionados)
        gestor_mascaras.dibujar_contornos(mascara_combinada, min_area=8000, max_area=20000000)

if __name__ == "__main__":
    main()
