import cv2
import numpy as np
# Cargar la imagen
imagen = cv2.imread('emile.png') 

# 1. Escala de Grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# 2. Umbralizacion
_, imagen_umbral = cv2.threshold(imagen_gris, 127, 255, cv2.THRESH_BINARY)

# 3. Inversion de colores
imagen_invertida = cv2.bitwise_not(imagen)

# 4. Ajuste de Brillo
imagen_brillante = cv2.add(imagen, (50, 50, 50))

# 5. Ajuste de Contraste
imagen_contraste = cv2.convertScaleAbs(imagen, alpha=1.5, beta=0)

# Mostrar resultados
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Escala de Grises', imagen_gris)
cv2.imshow('Umbralizacion', imagen_umbral)
cv2.imshow('Inversion de Colores', imagen_invertida)
cv2.imshow('Brillo Aumentado', imagen_brillante)
cv2.imshow('Contraste Aumentado', imagen_contraste)

cv2.waitKey(0)
cv2.destroyAllWindows()
