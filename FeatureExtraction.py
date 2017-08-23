import cv2
import os
from matplotlib import pyplot as plt
from PIL import Image


class FeatureExtractionTool:

    # Returns the contours of an image
    def getEdges(self, path, imName):
        img = cv2.imread(path+'/'+ imName)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(img, 200, 255, 3)
        return edges

    # Returns an image in greyscale format
    def getGreyscale(self, path, imName):
        img=cv2.imread(path + '/'+ imName)
        greyscl = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        greyscl = cv2.bitwise_not(greyscl)
        return greyscl

    # Returns a paired image. Paired image should have the same name as the original image
    # This can be useful for example if we want to do "Day to Night image translation"
    def makePair(self, path, imName):
        pairPath=input("Enter the path of the other image folder : ")
        return cv2.imread(pairPath + "/" + imName)

    # Puts the images in the input-output format required for pix2pix
    # The argument 'function' is one of the functions above-mentioned
    def featureExtraction(self, function, path):
         for image in os.listdir(path):
            print(image)
            img = Image.open(path+"/"+image)
            plt.subplot(121)
            plt.xticks([]), plt.yticks([])
            plt.imshow(img)
            plt.subplot(122),
            plt.xticks([]), plt.yticks([])
            plt.imshow(function(path, image), cmap='binary')
            plt.savefig(path+"/feature"+image)
