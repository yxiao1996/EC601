import sys
from PIL import Image

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