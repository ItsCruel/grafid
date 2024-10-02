import cv2
import numpy as np

# Abrir la camara 
video = cv2.VideoCapture(0)

# Comprobar si la cámara se pudo abrir
if not video.isOpened():
    print("Error al abrir la camara")
    exit()

while True:
    # Leer cada cuadro del video capturado por la camara
    ret, frame = video.read()

    if not ret:
        print("No se pudo obtener el cuadro")
        break

    # Convertir el cuadro de BGR a HSV
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definir el rango de color rojo en HSV
    bajo_rojo1 = np.array([0, 40, 40])
    alto_rojo1 = np.array([10, 255, 255])
    bajo_rojo2 = np.array([160, 40, 40])
    alto_rojo2 = np.array([180, 255, 255])

    # Crear una máscara para el color rojo
    mascara_rojo1 = cv2.inRange(frame_hsv, bajo_rojo1, alto_rojo1)
    mascara_rojo2 = cv2.inRange(frame_hsv, bajo_rojo2, alto_rojo2)
    mascara_rojo = cv2.add(mascara_rojo1, mascara_rojo2)

    # Convertir el cuadro original a escala de grises
    frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convertir la imagen gris a un formato BGR para que coincida con la original
    frame_gris_bgr = cv2.cvtColor(frame_gris, cv2.COLOR_GRAY2BGR)

    # Combinar el cuadro en gris con las áreas en rojo
    resultado = np.where(mascara_rojo[:, :, None] == 255, frame, frame_gris_bgr)

    # Mostrar el cuadro resultante
    cv2.imshow('Color resaltado', resultado)

    # Presionar 'q' para salir del video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
video.release()
cv2.destroyAllWindows()
