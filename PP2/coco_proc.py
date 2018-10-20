import os
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
        save_dir = "keras-yolo3/images/"
        for imgId in imgIds:
            img = self.coco.loadImgs(imgId)[0]
            img_path = self.dataDir + img['file_name']
            print(img_path)
            #try:
            I = cv2.imread(img_path)
            # cv2.imwrite(save_dir + img['file_name'], I)
            boxes, _ =  self._get_bound_box(img, catIds)
            I = self._draw_bound_box(I, boxes)
            cv2.imshow("Image Display", I)
            cv2.waitKey(10)
            #except:
            #    continue
            time.sleep(3)
        return

    def save_recognition(self, classes, save_dir, img_num):

        # --------------------------------- #
        # Save Images into folders for training recognition
        # --------------------------------- #

        # Check all class in classes is legitimate
        for c in classes:
            if (c not in self.cat_names):
                print("class not in coco: " + c)
                return

        catIds = self.coco.getCatIds(catNms=classes)
        imgIds = self.coco.getImgIds(catIds=catIds)

        # Check directories
        class_name = classes[0]
        save_folder = save_dir + class_name+'s'
        if (not os.path.exists(save_folder)):
            os.path.mkdir(save_folder)

        # Loop though the images
        for i, imgId in enumerate(imgIds):
            if (i == img_num):
                break
            img = self.coco.loadImgs(imgId)[0]
            img_path = self.dataDir + img['file_name']
            print(img_path)
            #try:
            I = cv2.imread(img_path)
            save_path = save_dir + class_name+'s' + '/' + class_name + "%03d"%i + ".jpg"
            cv2.imwrite(save_path, I)
            
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
        class_box = []
        for instance in anns:
            bbox = np.array(instance['bbox']).astype(int)
            class_ = instance['category_id']
            #print(instance)
            bound_box.append(bbox)
            class_box.append(class_)
        
        return  bound_box, class_box

    def gen_train_txt(self, classes, 
                      save_dir = '.\\keras-yolo3\\',
                      classes_save_dir = ".\\keras-yolo3\\model_data\\",
                      data_size = 0):

        # --------------------------------- #
        # Create training data file for YOLO: train_classes.txt, train.txt
        # Set argument data_size to 0 to generate all data
        # --------------------------------- #

        save_path = save_dir + "train_bear.txt"
        classes_save_path = classes_save_dir + "train_classes_bear.txt"
        save_file = open(save_path, "w")
        classes_save_file = open(classes_save_path, "w")

        # create a dictionary store category IDs
        class_dict = {}

        # Check all class in classes is legitimate
        class_count = 0
        for c in classes:
            if (c not in self.cat_names):
                print("class not in coco: " + c)
                return
            class_id = self.coco.getCatIds(c)
            class_dict[class_id[0]] = class_count
            class_count += 1
            classes_save_file.write(c + '\n')
        print(class_dict)

        catIds = self.coco.getCatIds(catNms=classes)
        imgIds = self.coco.getImgIds(catIds=catIds)

        # Loop though the images
        data_count = 0
        print("data size: " + str(len(imgIds)))
        for imgId in imgIds:
            
            if data_size != 0:
                if (data_count >= data_size):
                    break
                else:
                    data_count += 1

            new_line = ""  # Init a new line

            img = self.coco.loadImgs(imgId)[0]
            img_path = self.dataDir + img['file_name']
            new_line += img_path
            
            boxes, box_classes = self._get_bound_box(img, catIds)

            for i, box in enumerate(boxes):

                class_ = box_classes[i]
                if (class_ not in class_dict.keys()):
                    continue

                x_min = box[0]
                y_min = box[1]
                w = box[2]
                h = box[3]
                x_max = x_min + w
                y_max = y_min + h

                new_line += " " + str(x_min) + "," + str(y_min) + "," + str(x_max) + "," + str(y_max) + ","
                
                label = class_dict[class_]

                new_line += str(label) + ' '


            new_line += '\n'
            save_file.write(new_line)

        save_file.close()
        classes_save_file.close()
        print(data_count)
        
if __name__ == "__main__":

    sets = {'train': 'train2017',
                'val': 'val2017'}

    coco_path = 'D:\\downloads\\datasets\\'

    w = coco_worker(dataDir = coco_path,
                    dataType = sets['train'])

    classes = ['tennis racket']

    #w.loop_classes(classes)
    #w.gen_train_txt(classes)
    w.save_recognition(["elephant"], "recognistion/data/train/", 1000)