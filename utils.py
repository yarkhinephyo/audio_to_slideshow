import re
import nltk
import os
import shutil
from PIL import Image

VALID_POS = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', \
            'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS']

def get_expressions_removed(string):
    r = re.compile('%[\w]+')
    return r.sub('', string)

def get_pos_tags(string):
    tokenized = nltk.word_tokenize(string)
    tagged = nltk.pos_tag(tokenized)
    return tagged

def get_search_terms(pos_tags):
    len_pos_tags = len(pos_tags)
    search_terms = []
    skip = False
    for i in range(len_pos_tags):
        
        if skip:
            skip = False
            continue
        if (i < len_pos_tags - 1) and (pos_tags[i][1] in VALID_POS) and (pos_tags[i+1][1] in VALID_POS):
            search_terms.append((i, pos_tags[i][0] + ' ' + pos_tags[i+1][0]))
            skip = True
        elif pos_tags[i][1] in VALID_POS:
            search_terms.append((i, pos_tags[i][0]))
    print(search_terms)
    return search_terms

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