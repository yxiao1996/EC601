import os.path
import ffmpeg
import sys
sys.path.append(".\\vision")
from tweeimg.streamer import stream
from vision.funcs import *
from vision.utils import *
from vision.modules import ImageAnnotator

class App(object):

    def __init__(self, length = 10):

        self.buf_folder = "D:\\code_collection\\EC601\\EC601\\PP1\\tweeimg\\imgs"

        self.keypath = "C:/Users/xiaoy/Documents/keys/twitter/key.yaml"

        s = stream('@keinishikori',
                    key_path = self.keypath,
                    buf_folder = self.buf_folder,
                    buf_size = length) 

        self.length = length

        self.gen = s.streamImage()

        self.a = ImageAnnotator()

        count = 0

        pathLabelsDict = {}
        
        while(count < self.length - 1):

            count, image = next(self.gen)

            image_file = self.buf_folder + "/%03d" % count + ".jpg"

            if (os.path.isfile(image_file)):

                # using vision module to detect image labels

                self.a.loadImage(image)

                labels_raw = self.a.labelDetection()

                labels = []

                for label_raw in labels_raw:

                    labels.append(label_raw.description)

                pathLabelsDict[image_file] = labels

            else:

                print (image_file + " does not exist")

        # resize images

        resizeImage(self.buf_folder)

        # add labels to images

        addLabels(pathLabelsDict)

        # reform into video

        (
            ffmpeg
            .input(self.buf_folder + '/*.jpg', pattern_type='glob', framerate=2)
            .output('movie.mp4')
            .run()
        )

if __name__ == "__main__":

    app = App(10)