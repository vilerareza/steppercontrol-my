from steppermotor import StepperMotor
from undistorter import Undistorter
import subprocess
import cv2 as cv
import argparse
import json

# Argument handler
parser = argparse.ArgumentParser()
parser.add_argument('pattern', type = str)
#parser.add_argument('filename', type = str)
jsonDecoder = json.JSONDecoder()
# Unpack
args = parser.parse_args()
argPattern = args.pattern.replace("\'", "\"")
# Pattern
pattern = json.loads(argPattern)    # example: [{'dir':'f', 'steps': 1, 'mode':1, 'delay':0.05}]
# File Name
#fileName = args.filename

rawDir = "img_raw"
outDir = "img_corrected"
unDistorter = Undistorter(calFile='cal_data.p')
stepperMotor = StepperMotor()

def capture(rawDir, fileName):
    # Capture
    subprocess.run(['libcamera-still', '--denoise', 'off', '--shutter', '70000', '--gain', '0', '--awb', 'cloudy', '--immediate', '--rawfull', '-e', 'png', '-o', f'{rawDir}/{fileName}'])
    try:
        img = cv.imread(f'{rawDir}/{fileName}')
        return img
    except:
        print ('Image not found')

for i in range(len(pattern)):
    stepperMotor.move(dir = pattern[i]['dir'], steps = pattern[i]['steps'], mode = pattern[i]['mode'], delay=pattern[i]['delay'])
    img = capture(rawDir, 'temp.png')
    img_cor = unDistorter.undistort(img)
    cv.imwrite(f'{outDir}/{i}.png', img_cor)
    
