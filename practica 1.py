
import cv2 as cv

img = cv.imread('imagen',0)
cv.imshow('salida',img)
r,g,b=img.shape
for i in range(x):
    for j in range (y):
          if (img[i,j]>150):
                            img [i,j]=255
          else:        
                            img [i,j]=0

x,y,z=(img.shape,x,y,z)
print(img.shape, x , y , z)
cv.waitKey(0)
cv.destroyAllWindows()

#-END_SRC

#-RESULTS:
