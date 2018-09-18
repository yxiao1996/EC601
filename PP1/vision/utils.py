import sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from os import listdir

def crop(image, vertices):

    """ Cropping Image According to Vertices Provided """

    if (len(vertices) != 4):
        return None

    min_x = sys.maxint
    max_x = 0

    min_y = sys.maxint
    max_y = 0

    for vertex in vertices:

        x = vertex.x
        y = vertex.y

        if (x < min_x):
            min_x = x

        if (x > max_x):
            max_x = x

        if (y < min_y):
            min_y = y

        if (y > max_y):
            max_y = y

    box = (min_x, min_y, max_x, max_y)

    return image.crop(box)

def cropNormalized(image, vertices):

    if (len(vertices) != 4):
        return None

    width, height = image.size

    for vertex in vertices:

        vertex.x = int(vertex.x * width)
        vertex.y = int(vertex.y * height)

    min_x = sys.maxint
    max_x = 0

    min_y = sys.maxint
    max_y = 0

    for vertex in vertices:

        x = vertex.x
        y = vertex.y

        if (x < min_x):
            min_x = x

        if (x > max_x):
            max_x = x

        if (y < min_y):
            min_y = y

        if (y > max_y):
            max_y = y

    box = (min_x, min_y, max_x, max_y)

    return image.crop(box)

def resizeImage(path):

    max_height = 600

    max_width = 600

    files = listdir(path)

    if not path.endswith('/'):

        path = path + "/"

    for fn in files:

        if not fn.endswith("jpg"):

            continue

        image_file = path + fn

        image = Image.open(image_file)

        xsize, ysize = image.size

        ratio = float(ysize) / float(xsize)

        if (xsize < max_width and ysize < max_height):

            height = int(max_height * ratio)

            if height % 2 == 1:
                height += 1

            image = image.resize((max_width, height), Image.ANTIALIAS)

        elif (xsize < max_width):

            width = int(max_width / ratio)

            if width % 2 == 1:
                width += 1

            image = image.resize((width, max_height), Image.ANTIALIAS)

        else:

            height = int(max_height * ratio)

            if height % 2 == 1:
                height += 1

            image = image.resize((max_width, height), Image.ANTIALIAS)

        image.save(image_file)

def addLabels(pathLabelsDict):

    paths = pathLabelsDict.keys()

    for path in paths:

        image = Image.open(path)

        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype(font="college.ttf", size=16)

        labels = pathLabelsDict[path]

        for i, label in enumerate(labels):

            draw.text((0, 13 * i), label, (255, 255, 255), font=font)

        image.save(path)

if __name__ == "__main__":

    resizeImage("/home/yxiao1996/workspace/EC601/PP1/tweeimg/imgs")