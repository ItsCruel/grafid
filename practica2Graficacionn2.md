**Practica 2**

***Instrucciones***
Generar al menos cinco operadores puntuales utilizando la imagen generada o una imagen previamente cargada.

****descripción****
Este código  se usa para realizar diversas transformaciones sobre una imagen, como escala de grises, umbralización, inversión de colores, ajuste de brillo y ajuste de contraste. 

Estas líneas importan las bibliotecas Opencv y numpy:
python
import cv2
import numpy as np



Como paso 1 necesitamos cargar imagen , en mi caso use una de halo del personaje emile
python
imagen = cv2.imread('emile.png') 

Una vez carga la imagen  'emile.png'  la cambiamos por una variable llamada imagen.

Como primer operador vamos escalar la imagen a Escala de grises utilizando cv2.cvtColor. La conversión se hace de BGR 
python
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)


Como segundo operador decidi hacer una umbralización  se aplica un umbral binario a la imagen en escala de grises. Los píxeles con un valor superior a 127 se establecen en blanco (255), y los píxeles con un valor inferior se establecen en negro (0).

python
_, imagen_umbral = cv2.threshold(imagen_gris, 127, 255, cv2.THRESH_BINARY)


como tercer operador decidi hacer una Inversión de colores , con el bitwise not invierte los colores de la imagen original, transformando píxeles claros en oscuros y viceversa.
python
imagen_invertida = cv2.bitwise_not(imagen)





como cuarto operador hice un pequeño ajuste de brillo , aumente el brillo de la imagen sumando el valor (50, 50, 50) a cada canal de color (B, G, R), lo que hace que la imagen sea más clara.
python
imagen_brillante = cv2.add(imagen, (50, 50, 50))



como quinto operador  realice un ajuste de Contraste  con alpha=1.5 incrementa la pendiente de la transformación lineal, lo que intensifica las diferencias entre píxeles oscuros y claros. beta=0 no añade un desplazamiento adicional en la intensidad.
python
imagen_contraste = cv2.convertScaleAbs(imagen, alpha=1.5, beta=0)



y nada más queda mostrar resultados 
python
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Escala de Grises', imagen_gris)
cv2.imshow('Umbralizacion', imagen_umbral)
cv2.imshow('Inversion de Colores', imagen_invertida)
cv2.imshow('Brillo Aumentado', imagen_brillante)
cv2.imshow('Contraste Aumentado', imagen_contraste)

cv2.waitKey(0)
cv2.destroyAllWindows()

*****mostrando resultados****
- 'Imagen Original': Muestra la imagen original.

- 'Escala de Grises': Muestra la versión en escala de grises.

- 'Umbralizacion': Muestra la imagen umbralizada.

- 'Inversion de Colores': Muestra la imagen con los colores invertidos.

- 'Brillo Aumentado': Muestra la imagen con el brillo ajustado.

- 'Contraste Aumentado': Muestra la imagen con el contraste aumentado.

