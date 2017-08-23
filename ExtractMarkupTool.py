import pandas as pd
from PIL import Image, ImageDraw, ImageChops, ImageOps


class ExtractMarkupTool(object):
    CSV_COLUMN_INDEX_IMAGE_NAME = 0
    CSV_COLUMN_INDEX_REGION_SHAPE_ATTRIBUTES = 5

    def __init__(self, csv_path):
        self.csv_path = csv_path

    #Removes the characters in the csv file that are not used afterwards
    #Argument x_y stands for which coordinate (x or y) will be also removed
    def removeChar(self, element, x_y):
        element = element.replace('_%s":' % x_y, "")
        element = element.replace(',"', "")
        element = element.replace('[', "")
        element = element.replace(']', "")
        return element

    # Imports the .csv file extracted from VGG Image Annotator. Works for sure with only one region per frame.
    # Unfortunately, there are a lots of syntaxes that I could not use without deleting them to make the data usable
    def import_csv(self):
        data = pd.read_csv(self.csv_path)

        # Deletes images that are not labelled in the .csv file
        data = data[data.values[:, self.CSV_COLUMN_INDEX_REGION_SHAPE_ATTRIBUTES] != "{}"]

        data = pd.DataFrame(data.values[:, self.CSV_COLUMN_INDEX_REGION_SHAPE_ATTRIBUTES],
                             data.values[:, self.CSV_COLUMN_INDEX_IMAGE_NAME])

        file_names = [data.values[:, self.CSV_COLUMN_INDEX_IMAGE_NAME]]
        x = []
        y = []

        # Making the format readable
        for row in range(len(data)):
            file_names.append(data.values[row, 0].split(",")[0])
            x.append(data.values[row, 0].split("all_points")[1])
            y.append(data.values[row, 0].split("all_points")[2])

        xList = []
        yList = []

        # Making a list of x coordinates for each images
        for element in range(len(x)):
            self.removeChar(x[element], 'x')

        # Splitting them
        for element in x:
            xList.append(element.split(",", ))

        # Converting them to integers
        for element in xList:
            for value in range(len(element)):
                element[value] = int(element[value])

        # Same for the y coordinates
        for element in range(len(y)):
            self.removeChar(y[element], 'y')

        for element in y:
            yList.append(element.split(",", ))

        for element in yList:
            for value in range(len(element)):
                element[value] = int(element[value])

        return file_names, xList, yList

    # Creates a polygon used by the Image Draw module.
    # Converts the (x1, x2, ...), (y1, y2, ...) input in ((x1,y1),(x2,y2)) format
    def makePolygon(xList, yList):

        polygon = []
        for value in range(len(xList)):
            tuple = (xList[value], yList[value])
            polygon.append(tuple)
        return polygon

    # Returns the mask of the polygon
    def getMask(self, images, picture, original):
        polygon = self.makePolygon(images[1][picture], images[2][picture])
        mask = Image.new('RGB', original.size, color=(255, 255, 255))
        mask_draw = ImageDraw.Draw(mask)
        #Fills the are in black to get the mask
        mask_draw.polygon(polygon, fill=(0, 0, 0))
        return mask

    # Crops the image contained in the region
    def cropPictures(self, images, pathOriginal, pathSave):
        for picture in range(len(images[1])):
            original = Image.open(pathOriginal + "/" + images[0][0][picture])
            mask = self.getMask(images, picture, original)
            diff = ImageChops.lighter(original, mask)
            diff.save(pathSave + "/" + images[0][0][picture], "JPEG")

    # Creates a bounding box around the cropped image to keep only the "Not white only" area of the picture
    def centering(self, imgName, pathOriginal, pathSave):
        image = Image.open(pathOriginal + "/" + imgName)
        # An inverted copy of the image is created as getbbox works on black areas.
        invert_image = ImageOps.invert(image)
        box = invert_image.getbbox()
        image = image.crop(box)
        image.save(pathSave + "/" + imgName, "JPEG")
