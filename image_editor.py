#https://pillow.readthedocs.io/en/stable/installation.html#basic-installation
from PIL import Image, ImageFilter
# from PIL import ImageEnhance
import os

path = './imgs'
pathOut = '/editedImgs'

for filename in os.listdir(path):
    img= Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L') # convert on gray scale
    #edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90) #convert on gray scale and rotate the image
    # factor =1.5
    # enhacer = ImageEnhance.Contrast(edit)
    # edit = enhacer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f".{pathOut}/{clean_name}_edited.jpg")