import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('thx.png', 1)

# RGB a HSV
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Rojo
bajo_rojo1 = np.array([0, 40, 40])
alto_rojo1 = np.array([10, 255, 255])
bajo_rojo2 = np.array([160, 40, 40])
alto_rojo2 = np.array([180, 255, 255])

# Verde
bajo_verde = np.array([35, 40, 40])
alto_verde = np.array([85, 255, 255])

# Azul
bajo_azul = np.array([90, 40, 40])
alto_azul = np.array([130, 255, 255])

# Amarillo
bajo_amarillo = np.array([25, 40, 40])
alto_amarillo = np.array([35, 255, 255])

# Naranja
bajo_naranja = np.array([10, 40, 40])
alto_naranja = np.array([25, 255, 255])

# Crear de cada color
mascara_rojo1 = cv2.inRange(imagen_hsv, bajo_rojo1, alto_rojo1)
mascara_rojo2 = cv2.inRange(imagen_hsv, bajo_rojo2, alto_rojo2)
mascara_rojo = cv2.add(mascara_rojo1, mascara_rojo2)

mascara_verde = cv2.inRange(imagen_hsv, bajo_verde, alto_verde)
mascara_azul = cv2.inRange(imagen_hsv, bajo_azul, alto_azul)
mascara_amarillo = cv2.inRange(imagen_hsv, bajo_amarillo, alto_amarillo)
mascara_naranja = cv2.inRange(imagen_hsv, bajo_naranja, alto_naranja)

# Contar los objetos en cada masca
def contar_objetos(mascara):
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return len(contornos)

# contador de objetos 
objetos_rojos = contar_objetos(mascara_rojo)
objetos_verdes = contar_objetos(mascara_verde)
objetos_azules = contar_objetos(mascara_azul)
objetos_amarillos = contar_objetos(mascara_amarillo)
objetos_naranjas = contar_objetos(mascara_naranja)

# Imprimir resultados
print(f"Objetos rojos: {objetos_rojos}")
print(f"Objetos verdes: {objetos_verdes}")
print(f"Objetos azules: {objetos_azules}")
print(f"Objetos amarillos: {objetos_amarillos}")
print(f"Objetos naranjas: {objetos_naranjas}")


cv2.imshow('Objetos Rojos ', resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()
