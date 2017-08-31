# P2P Dataset Creation Tool




This repository consists in several scripts used to create a pix2pix dataset. It performs the following tasks :
* Capturing frames from a video (CollectTool.py)
* Cutting areas labelled using VGG Image Annotator (http://www.robots.ox.ac.uk/~vgg/software/via/) and crop the bounding box around that area (ExtractMarkupTool.py)
* Extract a feature from an image (edges, greyscale, or pairing images) and put them in the "Input - Output" format required for pix2pix (FeatureExtraction.py)
* Convert the set of images into CSV format (ImagesToCSVTool.py)



## CollectTool.py

This script helps in capturing the frames from videos in a folder.
The function AllVids helps in doing so.

Allvids requires two arguments :
*inputPath, the path to the folder containing the videos
*outputPath, the path to the folder where the frames should be saved. By default, it is equal to inputPath

Allvids will create a folder for each video in the inputPath.



##ExtractMarkupTool.py

After labelling the images using VGG Image Annotator, and saving the annotations into CSV format, you can use this script to extract the labelled areas of your image and isolate them from the original pictures.
To use this script, create an object with the path to the CSV file as attribute, then call the function cropAndCenterAll.

This function requires two arguments :
*pathOriginal, the path to the folder containing the images
*pathSave, the path to the folder where the cropped and centered images should be saved. 

WARNING : By default, pathSave is equal to pathOriginal, which means that **the images in pathOriginal will be overwritten**



##FeatureExtraction.py

This script transforms the images into the 'Input - Output' format required for training pix2pix.

Currently, this script contains only 3 extraction function :
*getEdges, which gives the edges of an image
*getGreyscale, which returns the image in greyscale
*makePair, which makes a pair of images.

To use this script, call the function featureExtraction.
This functions requires two arguments :
*function, which corresponds to one of the available extraction functions.
*path, which is the path to the folder containing the images

##ImageToCSVTool.py

This scripts transforms an image folder into a csv file.
To use this script, call the function imagesToCSV.
This function only requires two arguments :
*path, which is the path to the folder
*filename, which is the name of the created CSV file. This file will be saved in the above-mentionned path.
