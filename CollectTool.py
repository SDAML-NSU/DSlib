import cv2
import os


class CollectTool:

    # Captures the frames of videos located in the inputPath and stores them in the outputPath.
    # By default, outputPath=inputPath
    # The fps parameter is the frequency of frame capture per second, by default 2.
    def captureFramesFromVideo(self, inputPath, outputPath):
        if outputPath == "":
            outputPath = inputPath
        vidcap = cv2.VideoCapture(inputPath)
        success, image = vidcap.read()
        count = 0
        success = True
        while success:
            success, image = vidcap.read()
            cv2.imwrite(outputPath+"/"+"frame%d.jpg" % count, image)  # save frame as JPEG file
            count += 1

    # Captures frames from all the videos in a folder using captureFramesfromVideo
    # By default, outputPath=inputPath
    def allVids(self, inputPath, outputPath=''):
        if outputPath == "":
            outputPath = inputPath
        for file in os.listdir(inputPath):
            # Get the file name without the extension
            filename = os.path.splitext(file)[0]
            if not os.path.exists(outputPath + "/" + filename):
                os.makedirs(outputPath + "/" + filename)
            self.captureFramesFromVideo(inputPath + "/" + file, outputPath + "/" + filename)