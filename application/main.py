import os
import io

from google.cloud import vision
from library import floral

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'aritzia_hack.json'
client = vision.ImageAnnotatorClient()

# image = vision.Image()



# The name of the image file to annotate
file_name = os.path.abspath('/Users/leila/PycharmProjects/Aritzia/floral.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response_label = client.label_detection(image=image)

labels = set()
for label in response_label.label_annotations:
    if (label.score > 0.86):
        labels.add(label.description)
        print({'label': label.description, 'score': label.score})
if ("Dress" in labels) and ("Neck" in labels):
    print("here")
    floral()
# elif("blazer" and "turtleneck") in labels:
#     dark_ac()
# elif("vest") in labels:
#     preppy()
