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
