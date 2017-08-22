from PIL import Image
import numpy
import pandas as pd
import os


class ImageToCSVTool:


    #creates a CSV file containing images from a folder
    def imagesToCSV(path):
        columns = ['image','format', 'width', 'height', 'values']
        nameVec = []
        formatVec = []
        widthVec = []
        heightVec = []
        pixelStringVec = []
        for file in os.listdir(path):
            fileName = os.path.splitext(file)[0]
            fileFormat = os.path.splitext(file)[1]
            nameVec.append(fileName)
            formatVec.append(fileFormat)
            print(file)
            pixelString = ""
            img = Image.open(path + "/" + file)
            imgarray = numpy.array(img)
            heightVec.append(len(imgarray))
            widthVec.append(len(imgarray[0]))
            for line in range(len(imgarray)):
                for column in range(len(imgarray[line])):
                    pixelValue = imgarray[line][column]
                    if column == 0 & line == 0:
                        pixelString=pixelString + str(pixelValue)
                    else:
                        pixelString=pixelString + " " + str(pixelValue)
            pixelStringVec.append(pixelString)
        df = pd.DataFrame({'image':nameVec, 'format':formatVec, 'width':widthVec, 'height':heightVec, 'values':pixelStringVec}, columns=columns)
        print(df)
        df.to_csv(path+"/images.csv")


