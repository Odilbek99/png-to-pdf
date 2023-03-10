import os
import img2pdf
import glob
from PIL import Image


import re



def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

images_list = []
BASE_DIR = sorted_alphanumeric(os.listdir('./'))

for dir in BASE_DIR:
    for file in sorted_alphanumeric(os.listdir(dir)):
        if file.endswith(".png"):
            fpath = f'./{dir}/{file}'
            images_list.append(fpath)
            
with open('./11/output.pdf', 'wb' ) as f:
    f.write(img2pdf.convert(images_list))


