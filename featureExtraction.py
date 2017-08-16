import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import glob
from PIL import Image, ImageFilter, ImageOps, ImageDraw


class FeatureExtractionTool:

    def edging(self, path, imName):
    # Returns the contours of an image
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(img, 200, 255, 3)
        return(edges)

    def greyscale(self, path, imName):
    # Returns an image in greyscale format
        img=cv2.imread(path)
        greyscl = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        greyscl = cv2.bitwise_not(greyscl)
        return greyscl

    def pair(self, path, imName):
    # Returns a paired image. Paired image should have the same name as the original image
        pairPath=raw_input("Enter the path of the other image folder : ")
        return cv2.imread(pairPath+"/"+imName)


    def featureExtraction(self, function, path):
    # Puts the images in the format required for pix2pix
         for image in os.listdir(path):
            print(image)
            img = Image.open(path+"/"+image)
            plt.subplot(121)
            plt.xticks([]), plt.yticks([])
            plt.imshow(img)
            plt.subplot(122),
            plt.xticks([]), plt.yticks([])
            plt.imshow(function(path+"/"+image, image), cmap='binary')
            plt.savefig(path+"/feature"+image)

