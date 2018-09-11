import os.path
import ffmpeg

from tweeimg.streamer import stream
from vision.funcs import *


class App(object):

    def __init__(self, length = 10):

        s = stream('@keinishikori', buf_size = length)

        self.length = length

        self.gen = s.streamImage()

        self.buf_folder = "/home/yxiao1996/workspace/EC601/PP1/tweeimg/imgs"

        count = 0
        
        while(count < self.length - 1):

            count, image = self.gen.next()

            image_file = self.buf_folder + "/%03d" % count + ".jpg"

            if (os.path.isfile(image_file)):

                detect_labels(path = image_file, content = image)

            else:

                print image_file + " does not exist"

        (
            ffmpeg
            .input(self.buf_folder + '/*.jpg', pattern_type='glob', framerate=2)
            .crop(0, 0, 400, 200)
            .output('movie.mp4')
            .run()
        )

if __name__ == "__main__":

    app = App(4)