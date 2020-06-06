import shutil
import os
from PIL import Image

def navigate_up_directory(iteration):
    cwd = os.getcwd()
    for i in range(iteration):
        os.chdir("..")
    return cwd

def clear_images():
    shutil.rmtree(os.path.join(os.getcwd(), 'images'))

def clear_corrupted_images(image_folder):
    for folder in os.listdir(image_folder):
        for filename in os.listdir(os.path.join(image_folder, folder)):
            if filename.endswith('.jpg'):
                file_path = os.path.join(image_folder, folder, filename)
                try:
                    img = Image.open(file_path) # open the image file
                    img.verify() # verify that it is, in fact an image
                except (IOError, SyntaxError) as e:
                    print('Bad file:', filename) # print out the names of corrupt files
                    os.remove(file_path)