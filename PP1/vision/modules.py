import os
import io
import PIL
from PIL import Image
import numpy as np

from google.cloud import vision
from google.cloud.vision import types
from google.cloud import vision_v1p3beta1 as vision_beta

import utils

class ImageAnnotator(object):

    """ Annotate Image with Google vision API """

    def __init__(self):

        self.client = vision.ImageAnnotatorClient()
        self.client_beta = vision_beta.ImageAnnotatorClient()

        self.image = None

    def loadImage(self, image):

        """ Load Image into Annotator """

        self.image = image

    def labelDetection(self):

        """ Detect Labels in Image """

        if self.image == None:
            return

        image = vision.types.Image(content=self.image)

        labels = self.client.label_detection(image=image).label_annotations

        print labels
        return labels

    def cropHints(self, ratio = 0.618):

        """ Crop Region of Interest from image
            retrun: list[hints] """

        if self.image == None:
            return None

        image = vision.types.Image(content=self.image)

        crop_hints_params = vision.types.CropHintsParams(aspect_ratios=[ratio])
        image_context = vision.types.ImageContext(crop_hints_params=crop_hints_params)

        response = self.client.crop_hints(image=image, image_context=image_context)
        hints = response.crop_hints_annotation.crop_hints

        for n, hint in enumerate(hints):
            print('\nCrop Hint: {}'.format(n))

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                        for vertex in hint.bounding_poly.vertices])

            print('bounds: {}'.format(','.join(vertices)))

        return hints

    def localizeObjects(self):

        """ Localize Objects in Image 
            return: list[object]"""

        if self.image == None:
            return None

        image = vision_beta.types.Image(content=self.image)

        objects = self.client_beta.object_localization(image=image).localized_object_annotations

        print('Number of objects found: {}'.format(len(objects)))
        for object_ in objects:
            print('\n{} (confidence: {})'.format(object_.name, object_.score))
            print('Normalized bounding polygon vertices: ')
            for vertex in object_.bounding_poly.normalized_vertices:
                print(' - ({}, {})'.format(vertex.x, vertex.y))

        return objects

    def webDetection(self):

        """ Detect Web Links """

        if self.image == None:
            return None

        image = vision.types.Image(content=self.image)

        web_detection = self.client.web_detection(image=image).web_detection

        return web_detection

    def reportWebDetection(self, annotations):

        """Prints detected features in the provided web annotations."""
        if annotations.pages_with_matching_images:
            print('\n{} Pages with matching images retrieved'.format(
                len(annotations.pages_with_matching_images)))

            for page in annotations.pages_with_matching_images:
                print('Url   : {}'.format(page.url))

        if annotations.full_matching_images:
            print('\n{} Full Matches found: '.format(
                len(annotations.full_matching_images)))

            for image in annotations.full_matching_images:
                print('Url  : {}'.format(image.url))

        if annotations.partial_matching_images:
            print('\n{} Partial Matches found: '.format(
                len(annotations.partial_matching_images)))

            for image in annotations.partial_matching_images:
                print('Url  : {}'.format(image.url))

        if annotations.web_entities:
            print('\n{} Web entities found: '.format(
                len(annotations.web_entities)))

            for entity in annotations.web_entities:
                print('Score      : {}'.format(entity.score))
                print('Description: {}'.format(entity.description))


if __name__ == "__main__":

    path = '/home/yxiao1996/workspace/EC601/PP1/tweeimg/imgs/002.jpg'
    path_cropped = '/home/yxiao1996/workspace/EC601/PP1/tweeimg/imgs/002_c.jpg'
    path_cropped_buf = '/home/yxiao1996/workspace/EC601/PP1/tweeimg/imgs/buf/'
    a = ImageAnnotator()

    with io.open(path, 'rb') as image_file:
        img = image_file.read()

    a.loadImage(img)    

    hints = a.cropHints()

    img_jpg = Image.open(path)

    img_cropped = utils.crop(img_jpg, hints[0].bounding_poly.vertices)

    #img_cropped.show()
    
    img_cropped.save(path_cropped)

    with io.open(path_cropped, 'rb') as image_c_file:
        img_c = image_c_file.read()

    a.loadImage(img_c)

    objects = a.localizeObjects()

    img_jpg = Image.open(path_cropped)

    for i, object_ in enumerate(objects):

        print object_

        img_cropped = utils.cropNormalized(img_cropped, object_.bounding_poly.normalized_vertices)

        img_cropped.show()

        img_cropped_filename = path_cropped_buf + "%03d" % i + ".jpg"

        img_cropped.save(img_cropped_filename)

        with io.open(path_cropped, 'rb') as image_c_file:
            img_c = image_c_file.read()

        a.loadImage(img_c)

        anno = a.webDetection()

        a.reportWebDetection(anno)

        raw_input()