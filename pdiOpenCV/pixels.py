import numpy as np
import cv2 as cv
import os
import sys


INPUT_FOLDER = "..\input"
OUTPUT_FOLDER = "..\output"

def in_path(filename):
    return os.path.join(INPUT_FOLDER,filename)

def out_path(filename):
    return os.path.join(OUTPUT_FOLDER,filename)


if __name__ == "__main__":
    
    if not cv.useOptimized: cv.setUseOptimized(True)
    
    img = cv.imread(in_path("GYA001-1.JPG") )

    if img is None:
        sys.exit("Could not read the image.")

    # read pixel
    px = img[100,100]
    print( px )
    
    # alter one pixel
    img[100,100] = [255,255,255]
    print( img[100,100] )
    
    # accessing RED value
    print(img.item(10,10,2))
    
    # modifying RED value
    img.itemset((10,10,2),100)
    print(img.item(10,10,2))
   
    # showing the properties 
    print( img.shape )
    print( img.size )
    print( img.dtype )
    
    # Region of interest (ROI)
    pict = img[280:340, 330:390]
    img[273:333, 100:160] = pict
    
    # split and merge the cannels
    b,g,r = cv.split(img)
    img = cv.merge((b,g,r))
    
    
    cv.imshow('image',img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
  
