from PIL import Image
import numpy
import pandas as pd
import os


#class ImageToCSVTool:

def imagesToCSV(path):
    columns=['image','format', 'width', 'height', 'values']
    nameVec=[]
    formatVec=[]
    widthVec=[]
    heightVec=[]
    pixelStringVec=[]
    for file in os.listdir(path):
        nameVec.append(file[:-4])
        formatVec.append(file[-3:])
        width=0
        height=0
        print(file)
        pixelString=""
        img = Image.open(path + "/" + file)
        imgarray = numpy.array(img)
        heightVec.append(len(imgarray))
        widthVec.append(len(imgarray[0]))
        for line in range(len(imgarray)):
            for column in range(len(imgarray[line])):
                pixelValue=imgarray[line][column]
                if column==0 & line==0:
                    pixelString=pixelString + str(pixelValue)
                else:
                    pixelString=pixelString + " " + str(pixelValue)
        pixelStringVec.append(pixelString)
    df = pd.DataFrame({'image':nameVec, 'format':formatVec, 'width':widthVec, 'height':heightVec, 'values':pixelStringVec}, columns=columns)
    print(df)
    return(df)


path="C:/Users/Vladimir/Desktop/Mickey Dataset/V1/Test2"
imagesToCSV(path)