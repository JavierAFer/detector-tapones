from clases import GestorImagenes, GestorMascaras
import cv2

def mostrar_menu_colores():
    """Mostrar la lista de colores disponibles para elegir"""
    colores_disponibles = [
        "negro", "blanco", "azul claro", "rojo", "azul", 
        "rosa claro", "rosa fuerte"
    ]
    print("Colores disponibles:")
    for idx, color in enumerate(colores_disponibles, 1):
        print(f"{idx}. {color}")
    print("\nTambién puedes elegir 'mascara completa' para seleccionar todos los colores.\n")
    return colores_disponibles

def procesar_imagen(gestor_mascaras, colores_seleccionados, colores_disponibles):
    """Procesa una imagen con las máscaras seleccionadas"""
    if "mascara completa" in colores_seleccionados:
        mascara_completa = gestor_mascaras.combinar_mascaras(colores_disponibles)
        gestor_mascaras.dibujar_contornos(mascara_completa)
    else:
        # Combinar las máscaras para los colores seleccionados
        mascara_combinada = gestor_mascaras.combinar_mascaras(colores_seleccionados)
        gestor_mascaras.dibujar_contornos(mascara_combinada)


def main():
    colores_disponibles = mostrar_menu_colores()
    color_elegido = input("Introduce los colores que deseas (separados por comas) o 'mascara completa': ").lower()
    colores_seleccionados = [color.strip() for color in color_elegido.split(',')]

    gestor_imagenes = GestorImagenes("./images")
    imagenes = gestor_imagenes.cargar_y_copiar_imagenes()

    if not imagenes:
        print("No se encontraron imágenes.")
        return

    procesar_todas = input("¿Quieres procesar todas las imágenes? (si/no): ").lower()

    if procesar_todas == "si":
        for idx, imagen in enumerate(imagenes):
            print(f"\nProcesando imagen {idx + 1}/{len(imagenes)}...")
            gestor_mascaras = GestorMascaras(imagen)
            procesar_imagen(gestor_mascaras, colores_seleccionados, colores_disponibles)
    elif procesar_todas == "no":
        imagen_idx = int(input(f"Introduce el número de la imagen que deseas procesar (1-{len(imagenes)}): ")) - 1
        if 0 <= imagen_idx < len(imagenes):
            imagen = imagenes[imagen_idx]
            gestor_mascaras = GestorMascaras(imagen)
            procesar_imagen(gestor_mascaras, colores_seleccionados, colores_disponibles)
        else:
            print("Número de imagen no válido.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()