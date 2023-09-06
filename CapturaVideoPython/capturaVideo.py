import cv2 as cv 

import numpy as np




if __name__ == "__main__":


    camera = cv.VideoCapture(0)
    rodando = True

    while rodando:

        status, frame = camera.read()

        if not status or cv.waitKey(1) & 0xff == ord('q'):
            rodando = False
        
        cv.imshow("Camera", frame)
        rodando == False
        
    print(camera.get(CV_CAP_PROP_FRAME_WIDTH))
