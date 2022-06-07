#import argparse
import os
import cv2 as cv
import numpy as np

imgDir = "img_corrected"
fileName1 = '1.png'
fileName2 = '2.png'
img1 = cv.imread(f'{imgDir}/{fileName1}')
img2 = cv.imread(f'{imgDir}/{fileName2}')
