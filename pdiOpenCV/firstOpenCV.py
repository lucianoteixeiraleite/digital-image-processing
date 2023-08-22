import numpy as np
import cv2
from matplotlib import pyplot as plt

obj_img = cv2.imread("GYA001-1.JPG")
obj_img = obj_img[180 : 980, 240: 840]
obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)


def colorGray(image):
    altura, largura, canais_de_cor = image.shape
    for y in range(altura):
        for x in range(largura):
            vermelho = image.item(y,x,0)
            verde    = image.item(y,x,1)
            azul     = image.item(y,x,2)
            lum = int(0.3*vermelho + 0.59*verde + 0.11*azul)
            image.itemset((y,x,0),lum)
            image.itemset((y,x,1),lum)
            image.itemset((y,x,2),lum)
    return image

def insertBorder(image):
    return cv2.copyMakeBorder(image,1,1,1,1,cv2.BORDER_CONSTANT,(255,255,255))

def displayImagesHorizontally(imgsArray):
    
    if len(imgsArray) == 0:
        return
    else:
        countDraw =  len(imgsArray)
        
    fig = plt.figure(figsize=(14, 14))
          
    for i in range(0,len(imgsArray)):
        fig.add_subplot(1,countDraw,i+1)
        plt.imshow(imageArray[i])
       
    plt.show()
   
    return
    
 
if __name__ == "__main__":
    
    obj_img = colorGray(obj_img)            #turns to grayscale
    obj_img = insertBorder(obj_img)         #insert the borders
    imageArray = np.array([obj_img],dtype='uint8')
    
    
    
    
    
    
    
    
    
    displayImagesHorizontally(imageArray)
    
    