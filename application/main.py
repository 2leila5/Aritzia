import os
import io
from google.cloud import vision


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'aritzia_hack.json'
client = vision.ImageAnnotatorClient()

# image = vision.Image()
# image.source.image_uri = "aritzia_hack.json"


# The name of the image file to annotate
file_name = os.path.abspath('../floral.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)


response_label = client.label_detection(image=image)

for label in response_label.label_annotations:
    print({'label': label.description, 'score': label.score})
