from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def in_path(filename):
    return os.path.join(INPUT_FOLDER,filename)

def out_path(filename):
    return os.path.join(OUTPUT_FOLDER,filename)

original_image = Image.open(in_path("GYA001-1.JPG"))
box = (300, 0, original_image.width//2, original_image.height//2)
original_image = original_image.crop(box)
    
#####################################################################    
def grayscale(colored):
    w , h = colored.size
    img = Image.new(colored.mode, (w,h))

    for y in range(w):
        for x in range(h):
            pxl = colored.getpixel((y,x))
            lum = int(0.3*pxl[0] + 0.59*pxl[1] + 0.11*pxl[2])
            img.putpixel((y,x),(lum,lum,lum))
    
    return img
#####################################################################
def show_vertical(im1,im2):
    im = Image.fromarray(np.hstack((np.array(im1),np.array(im2))))
    im.show()
####################################################################    
def filtroNegativo(image):
    w , h = image.size
    COLOR = (255,255,255)
    new_image = Image.new(image.mode,(image.width,image.height),COLOR)
    
    for y in range(w):
        for x in range(h):
              
            pxl = image.getpixel((y,x))
            r = 255 - pxl[0] 
            g = 255 - pxl[1] 
            b = 255 - pxl[2] 
            new_image.putpixel((y,x),(r,g,b))
 
    
    return new_image
#####################################################################
def filtroGamma(image,gamma):
    w , h = image.size
    COLOR = (255,255,255)
    new_image = Image.new(image.mode,(image.width,image.height),COLOR)
    
    for y in range(w):
        for x in range(h):
              
            pxl = image.getpixel((y,x))
            r = int((pxl[0]/255) ** gamma * 255) 
            g = int((pxl[1]/255) ** gamma * 255) 
            b = int((pxl[2]/255) ** gamma * 255) 
            new_image.putpixel((y,x),(r,g,b))
 
    
    return new_image
#####################################################################        
def grafico3D(img):
    import matplotlib.pyplot as plt
    from mpl_toolkits import mplot3d
    import numpy as np
    from matplotlib.colors import LightSource
    
    axeY = [] 
    axeX = []
    axeZ = []
       
    for y in range(img.width) : 
        for x in range(img.height) : 
            axeY.append(y) 
            axeX.append(x) 
            pxl = img.getpixel((y,x))
            axeZ.append(pxl[0]) 
    
    
    fig = plt.figure(figsize=(800,600))
    ax = fig.add_subplot(projection='3d')
   
    ax.scatter3D(axeX, axeY, axeZ, c='gray', s=0.1,  marker= ',')
    ax.view_init(elev=-90, azim=90)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_zlim(0,200)

    plt.show()
#####################################################################    
def corte(img):
    for y in range(img.width) : 
        for x in range(img.height) :
            if img.getpixel((y,x))[0] > 200: 
               img.putpixel((y,x),(0,0,0))
               
            
    return img   
#####################################################################
def criaHistograma(img):
    import matplotlib.pyplot as plt
    h = np.zeros(256)
    for y in range(img.width):
        for x in range(img.height):
            h[img.getpixel((y,x))[0]] += 1
            
    eixo_x = list(range(256))
    plt.figure(2)
    plt.bar(eixo_x,h)
    plt.show()  
#####################################################################    
def grid(img,largura):
    for y in range(img.width):
        if ((y % largura) == 0):
            for x in range(img.height):
                img.putpixel((y,x),(0,0,0)) 
    for x in range(img.height):
        if ((x % largura) == 0):
            for y in range(img.width):
                img.putpixel((y,x),(0,0,0))             
    return img      
    
#####################################################################   

def show_edges_sobel(img, offset=0, direction='x'):
    from  math import sqrt 
            
    XSOBEL = ImageFilter.Kernel(
    (3,3),
     [ -1, 0, 1,
       -2, 0, 2,
       -1, 0, 1],
     1,
     offset ) 
                          

    YSOBEL = ImageFilter.Kernel(
    (3,3),
     [ -1, -2, -1,
        0,  0, 0,
        1,  2, 1],
     1,
     offset )  
    
    if direction == 'y':
        filtered = img.filter(YSOBEL)
    elif direction == 'x':
        filtered = img.filter(XSOBEL)
    else:
        hsobel = img.filter(YSOBEL)
        vsobel = img.filter(XSOBEL)
        w, h = img.size
        filtered = img
        for y in range(w):
            for x in range(h):
                value = sqrt(
                    vsobel.getpixel((y,x))[0]**2 + hsobel.getpixel((y,x))[0]**2
                )
                value = int(min(value,255))
                filtered.putpixel((y,x),(value,value,value))
    return filtered
#####################################################################
def show_edges_prewitt(img, offset=0, direction='x'):
    from  math import sqrt 
            
    XPREWITT = ImageFilter.Kernel(
    (3,3),
     [ 1, 0, -1,
       1, 0, -1,
       1, 0, -1],
     1,
     offset ) 
                          

    YPREWITT = ImageFilter.Kernel(
    (3,3),
     [ 1,   1,  1,
       0,   0,  0,
       -1, -1, -1],
     1,
     offset )  
    
    if direction == 'y':
        filtered = img.filter(YPREWITT)
    elif direction == 'x':
        filtered = img.filter(XPREWITT)
    else:
        hprewitt = img.filter(YPREWITT)
        vprewitt = img.filter(XPREWITT)
        w, h = img.size
        filtered = img
        for y in range(w):
            for x in range(h):
                value = sqrt(
                    vprewitt.getpixel((y,x))[0]**2 + hprewitt.getpixel((y,x))[0]**2
                )
                value = int(min(value,255))
                filtered.putpixel((y,x),(value,value,value))
    return filtered

 
if __name__ == "__main__":

    final_image = grayscale(original_image)
    
    #final_image.save(out_path("saida.jpg"))
    
    #filtered = final_image.filter(ImageFilter.EMBOSS)
    
    #filtered = filtroNegativo(final_image)
    
    #filtered = filtroGamma(final_image,1.8)
    
    #show_vertical(final_image,filtered)
            
    #grafico3D(corte(final_image))
    
    #criaHistograma(final_image)
    
    #grid = grid(final_image,50)
    #grid.show()
    #final_image.show()
    
    #show_vertical(show_edges_sobel(final_image,50,'y'), show_edges_sobel(final_image,50,'x'))
    #show_vertical(show_edges_sobel(final_image,0,'a'),final_image)
    
    #show_vertical(show_edges_prewitt(final_image,50,'y'), show_edges_prewitt(final_image,50,'x'))
    show_vertical(show_edges_prewitt(final_image,0,'a'),final_image)
    







