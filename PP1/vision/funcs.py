import io
import os

from google.cloud import vision
from google.cloud.vision import types

def detect_landmarks(path, content = None):
    """Detects landmarks in the file."""
    client = vision.ImageAnnotatorClient()

    if (content == None):
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    print('Landmarks:')

    for landmark in landmarks:
        print(landmark.description)
        for location in landmark.locations:
            lat_lng = location.lat_lng
            print('Latitude {}'.format(lat_lng.latitude))
            print('Longitude {}'.format(lat_lng.longitude))

def detect_labels(path, content = None):

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    if (content == None):
        # Loads the image into memory
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)

def detect_faces(path, content = None):
    """Detects faces in an image."""
    client = vision.ImageAnnotatorClient()

    if (content == None):
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))

if __name__ == '__main__':
    detect_faces('/home/yxiao1996/workspace/EC601/PP1/tweeimg/imgs/002.jpg')