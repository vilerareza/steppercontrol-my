#import argparse
import os
import cv2 as cv
import numpy as np
import pickle

imgDir = "img_raw"
outDir = "img_corrected"
# Argument handler
#parser = argparse.ArgumentParser()
#parser.add_argument('dir', type = str, default = '')

#args = parser.parse_args()

# Loading calibration data
try:
    camera_cal = pickle.load(open('../camera_cal.p',"rb"))
    mtx = camera_cal["mtx"]
    dist = camera_cal["dist"]
except:
    print ('Calibration data does not exist')

try:
    imageFiles = os.listdir(imgDir)
    if len(imageFiles) > 0:
        for imageFile in imageFiles:
            filePath = os.path.join(imgDir, imageFile)
            img = cv.imread(filePath)
            # Undistort image with camera calibration data
            undst_image = cv.undistort(img, mtx, dist, None, mtx)
            cv.imwrite(f'{outDir}/{imageFile}',undst_image)
    else:
        print ('Source image does not exist')
except:
    print ('Source directory not found')
