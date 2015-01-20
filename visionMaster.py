import cv2
import sys

import imageSimple as imgSi

helpArgs = []
helpArgs.append('   -rc    Shows raw contours being found')
helpArgs.append('   -tf    Shows tape being found')
helpArgs.append('   -img   Image input (Must be followed by path)')

rawContours = False
findTape = False
imageInput = False
imagePath = None
running = True


if len(sys.argv) != 1:
    skip = False
    for i in range(1, len(sys.argv)):
        if skip == True:
            skip = False
        else:
            current = sys.argv[i]
            if current == '-rc':
                rawContours = True

            elif current == '-tf':
                findTape = True
            elif current == '-img':
                imageInput = True
                i += 1
                imagePath = sys.argv[i]
                skip = True
                if len(sys.argv) == 3:
                    rawContours = True
            elif current == '--help':
                running = False
                for tip in helpArgs:
                    print tip
            else:
                running = False
                for tip in helpArgs:
                    print tip
else:
    rawContours = True

#Determining content
waitTime = None
content = None
if imageInput:
    content = cv2.imread(imagePath)
    waitTime = 0
else:
    content = cv2.VideoCapture(0)
    waitTime = 1

imgSi.run(content, rawContours, findTape, waitTime, imageInput, running)
