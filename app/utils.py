import shutil
import os
from PIL import Image

def navigate_up_directory(iteration):
    """Navigate current directory up some iteration.
    Used when compiled into executable.

    Args:
        iteration (int): Number of directories to go above

    Returns:
        str: New directory path
    """
    cwd = os.getcwd()
    for i in range(iteration):
        os.chdir("..")
    return cwd

def clear_images():
    """ Clear ./images directory
    """
    shutil.rmtree(os.path.join(os.getcwd(), 'images'))

def clear_corrupted_images(images_folder):
    """Clear corrupted images

    Args:
        images_folder (str): Path of images folder
    """
    for folder in os.listdir(images_folder):
        for filename in os.listdir(os.path.join(images_folder, folder)):
            if filename.endswith('.jpg'):
                file_path = os.path.join(images_folder, folder, filename)
                try:
                    img = Image.open(file_path) # open the image file
                    img.verify() # verify that it is, in fact an image
                except (IOError, SyntaxError) as e:
                    print('Bad file:', filename) # print out the names of corrupt files
                    os.remove(file_path)