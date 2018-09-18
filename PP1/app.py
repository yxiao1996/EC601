import os.path
import ffmpeg

from tweeimg.streamer import stream
from vision.funcs import *
from vision.utils import *
from vision.modules import ImageAnnotator


class App(object):

    def __init__(self, length = 10):

        s = stream('@keinishikori', buf_size = length)

        self.length = length

        self.gen = s.streamImage()

        self.a = ImageAnnotator()

        self.buf_folder = "/home/yxiao1996/workspace/EC601/PP1/tweeimg/imgs"

        count = 0

        pathLabelsDict = {}
        
        while(count < self.length - 1):

            count, image = self.gen.next()

            image_file = self.buf_folder + "/%03d" % count + ".jpg"

            if (os.path.isfile(image_file)):

                #detect_labels(path = image_file, content = image)

                self.a.loadImage(image)

                labels_raw = self.a.labelDetection()

                labels = []

                for label_raw in labels_raw:

                    labels.append(label_raw.description)

                pathLabelsDict[image_file] = labels

            else:

                print image_file + " does not exist"

        # resize images

        resizeImage("./tweeimg/imgs/")

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