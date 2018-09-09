import os.path

from tweeimg.streamer import stream
from vision.funcs import *


class App(object):

    def __init__(self):

        s = stream('@keinishikori')

        self.gen = s.streamImage()

        self.buf_folder = "/home/yxiao1996/workspace/EC601/PP1/tweeimg/imgs"

        while(True):

            count, image = self.gen.next()

            image_file = self.buf_folder + "/%03d" % count + ".jpg"

            if (os.path.isfile(image_file)):

                detect_labels(path = image_file, content = image)

            else:

                print image_file + " does not exist"

            

if __name__ == "__main__":

    app = App()