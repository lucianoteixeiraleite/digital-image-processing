import cv2 as cv
import numpy as np
import sys
import os

INPUT_FOLDER = "..\input"
OUTPUT_FOLDER = "..\output"

def in_path(filename):
    return os.path.join(INPUT_FOLDER,filename)

def out_path(filename):
    return os.path.join(OUTPUT_FOLDER,filename)


if __name__ == "__main__":
    
    img = cv.imread(in_path("GYA001-1.JPG"))

    if img is None:
        sys.exit("Could not read the image.")

    cv.imshow("Display window", img)

    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite(out_path("GYA001-1.JPG"), img)
       

