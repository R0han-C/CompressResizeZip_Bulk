#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import glob
import shutil
import zipfile
from PIL import Image

path = os.walk('.')
folders = []
for (root, directories, files) in path:
    for directory in directories:
        folders.append(directory)

paths = []
for i in folders:
    paths.append(os.getcwd() + '\\' + i + '\\')

for i in paths:
    os.chdir(i)
    files_in_sub = os.listdir()
    for img in files_in_sub:
        image_ = Image.open(img)
        file_name_resized = 'RESIZED-' + img
        file_name_compressed = 'COMPRESSED-' + img
        image_resize = image_.resize((50, 50), Image.ANTIALIAS)
        image_resize.save(file_name_resized)
        image_.save(file_name_compressed, quality=30)
        image_.close()
        image_resize.close()

os.chdir('..')
if os.path.exists('OUTPUT'):
    shutil.rmtree('OUTPUT')
if not os.path.exists('OUTPUT'):
    os.makedirs('OUTPUT')


def zipdir(path, ziph):

    # ziph is zipfile handle

    for (root, dirs, files) in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


zipf = zipfile.ZipFile('OUTPUT.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir(os.getcwd(), zipf)
zipf.close()

shutil.move(os.getcwd() + '\OUTPUT.zip', os.getcwd() + '\OUTPUT')
