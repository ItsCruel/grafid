**PRACTICA 1**

**DESCRIPCIÓN**

Para esta práctica se solicitó que  generáramos una imagen tipo pixel art utilizando una matriz de enteros en el rango de 0 a 255.

como paso 0 decidi que queria hacer un champiñon estilo minecraft 

![champiñonminecraft](hongo.png)

como paso 1 se creó una imagen yo decidí hacerla de 500 x 500 píxeles , el tipo de dato uint8 quiere decir que cada valor de píxel tiene 8 bits y luego se multiplicó por 240 que da un fondo de gris clarito

img = np.ones((500, 500), dtype=np.uint8) * 240

para la parte 2 comenzamos a detallar el champiñón , con el tronco

 

for i in range(200, 260):  

    for j in range(230, 270):  

        img[i, j] = 60

utilizando esta pieza de código se crea un rectángulo , utilizando (200, 230) a (259, 269),  crea una sección vertical de 60 x 40 píxeles , los valores de los pixeles se establecen en 60 para darle un color más oscuro al tronco del hongo.

para la parte de arriba del hongo utilizamos este código:

for i in range(140, 200):  

    for j in range(180, 320):  

        img[i, j] = 100

Se utiliza para generar un rectángulo en forma horizontal , los píxeles van desde (140,180 ) a (199 ,319) creando el rectángulo de 60 x 140 píxeles.

**Mostrando Imagen **

por último queda mostrar el resultado del pixel art 

![champiñon pixel art](pixelhongo.png)
