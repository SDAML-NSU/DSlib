import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import glob
from PIL import Image, ImageFilter, ImageOps, ImageDraw


class FeatureExtractionTool:

    def edging(path):
    # Returns the contours of an image
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(img, 200, 255, 3)
        return(edges)

    def greyscale(path):
        img=cv2.imread(path)
        greyscl = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        greyscl = cv2.bitwise_not(greyscl)
        return greyscl


    def featureExtraction(function, path):
    # Puts the images in the format required for pix2pix
         for image in os.listdir(path):
            print(image)
            img = Image.open(path+"/"+image)
            plt.subplot(121)
            plt.xticks([]), plt.yticks([])
            plt.imshow(img)
            plt.subplot(122),
            plt.xticks([]), plt.yticks([])
            plt.imshow(function(path+"/"+image), cmap='binary')
            plt.savefig(path+"/feature"+image)

