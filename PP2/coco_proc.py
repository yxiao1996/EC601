from pycocotools.coco import COCO
import pycocotools.mask as mask
import os, sys, zipfile
import urllib.request
import shutil
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import cv2
import time
import numpy as np
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

class coco_worker(object):

    # --------------------------------- #
    # Extract certain class f images from coco dataset
    # --------------------------------- #

    def __init__(self,
                 dataDir = 'D:\\downloads\\datasets\\',
                 dataType = 'train2017'):

        dataDir = dataDir + dataType + '\\'
        self.dataDir = dataDir
        self.dataType = dataType

        # build some more pathes
        self.annDir = '{}annotations'.format(dataDir)
        self.annZipFile = '{}\\annotations_train{}.zip'.format(dataDir, dataType)
        self.annFile = '{}\\instances_{}.json'.format(self.annDir, dataType)
        self.annURL = 'http://images.cocodataset.org/annotations/annotations_train{}.zip'.format(dataType)

        # Initialize coco dataset API
        self.coco = COCO(self.annFile)
        
        # Load coco categories
        self.cats = self.coco.loadCats(self.coco.getCatIds())
        self.cat_names = [cat['name'] for cat in self.cats]
        print('COCO categories: \n{}\n'.format(' '.join(self.cat_names)))

        # Load coco superclasses
        self.supercat_names = set(cat['supercategory'] for cat in self.cats)
        print('COCO supercategories: \n{}'.format(' '.join(self.supercat_names)))

        return

    def loop_classes(self, classes):

        # --------------------------------- #
        # Loop through images contains classes
        # --------------------------------- #

        # Check all class in classes is legitimate
        for c in classes:
            if (c not in self.cat_names):
                print("class not in coco: " + c)
                return

        catIds = self.coco.getCatIds(catNms=classes)
        imgIds = self.coco.getImgIds(catIds=catIds)

        # Loop though the images
        for imgId in imgIds:
            img = self.coco.loadImgs(imgId)[0]
            img_path = self.dataDir + img['file_name']
            print(img_path)
            try:
                I = cv2.imread(img_path)
                boxes =  self._get_bound_box(img, catIds)
                I = self._draw_bound_box(I, boxes)
                cv2.imshow("Image Display", I)
                cv2.waitKey(10)
            except:
                continue
            time.sleep(3)
        return
    
    def _draw_bound_box(self, img, boxes):

        # --------------------------------- #
        # Draw bounding boxes to an image and return
        # --------------------------------- #

        for box in boxes:

            x = box[0]
            y = box[1]
            w = box[2]
            h = box[3]

            lt = (int(x), int(y))
            rb = (int(x + w), int(y + h))

            cv2.rectangle(img, lt, rb, (255, 0, 0))

        return img

    def _get_bound_box(self, img, catIds):
        
        # --------------------------------- #
        # Return bounding box of a coco image
        # --------------------------------- #

        annIds = self.coco.getAnnIds(imgIds = img['id'],
                                     catIds = catIds,
                                     iscrowd = None)

        anns = self.coco.loadAnns(annIds)

        #print (anns)
        bound_box = []
        for instance in anns:
            bbox = np.array(instance['bbox']).astype(int)
            print(bbox)
            bound_box.append(bbox)
        
        return  bound_box

if __name__ == "__main__":

    sets = {'train': 'train2017',
                'val': 'val2017'}

    coco_path = 'D:\\downloads\\datasets\\'

    w = coco_worker(dataDir = coco_path,
                    dataType = sets['val'])

    classes = ['chair']

    w.loop_classes(classes)