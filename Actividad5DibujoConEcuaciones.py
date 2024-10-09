import cv2
import numpy as np

# Crear una imagen en blanco de 500x500 
imagen = np.zeros((500, 500, 3), dtype="uint8")

# Dibujar la cabeza (círculo)
cv2.circle(imagen, (250, 150), 50, (255, 0, 0), -1)  # cabeza azul

# Dibujar el cuerpo (rectángulo)
cv2.rectangle(imagen, (220, 200), (280, 350), (255, 0, 0), -1)  # cuerpo azul

# Dibujar los brazos (líneas)
cv2.line(imagen, (220, 220), (150, 300), (255, 0, 0), 5)  # brazo izquierdo azul
cv2.line(imagen, (280, 220), (350, 300), (255, 0, 0), 5)  # brazo derecho azul

# Dibujar las piernas (líneas)
cv2.line(imagen, (240, 350), (200, 450), (255, 0, 0), 5)  # pierna izquierda azul
cv2.line(imagen, (260, 350), (300, 450), (255, 0, 0), 5)  # pierna derecha azul

# Mostrar la imagen resultante
cv2.imshow('Persona', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
