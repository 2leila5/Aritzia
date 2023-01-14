import os
import io
from google.cloud import vision
import library

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'aritzia_hack.json'
client = vision.ImageAnnotatorClient()

# image = vision.Image()
# image.source.image_uri = "aritzia_hack.json"


# The name of the image file to annotate
file_name = os.path.abspath('/Users/leila/PycharmProjects/Aritzia/floral.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response_label = client.label_detection(image=image)

for image in loaded_images:
    for label in response_label.label_annotations:
        if (label.score > 0.86):
            labels = [label.description.tostring]
            print({'label': label.description, 'score': label.score})
    if ("dress"  and "neck")  in labels :
        plt.imshow(np.array(training_data[0]).reshape(80, 80, 3))

