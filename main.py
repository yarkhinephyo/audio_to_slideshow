from audio_parser import get_text_from_audio
from utils import *
from flickr_scraper import get_urls
from image_edit import add_text_to_image, save_gif
import os

wav_dir = os.path.join(os.getcwd(), "wav_files")
audio_file = os.path.join(os.getcwd(), "wav_files", os.listdir(wav_dir)[0])

def handle_audio_file(audio_file):
    parsed_text = get_text_from_audio(audio_file)
    cleaned_text = get_expressions_removed(parsed_text)
    pos_tags = get_pos_tags(cleaned_text)
    search_terms = get_search_terms(pos_tags)

    for pos, search_term in search_terms:
        get_urls(search_term, str(pos), n=3, download=True)

    return get_sentences(pos_tags, search_terms)

def add_text_to_images(sentences):
    save_paths = []

    save_folder = os.path.join(os.getcwd(), 'images', 'final')
    if not os.path.isdir(save_folder):
        os.mkdir(save_folder)
    images_path = os.path.join(os.getcwd(), 'images')

    # Sort the folders after converting to integers
    sorted_folders = sorted([int(name) for name in os.listdir(images_path) if name != 'final'])

    for i, folder in enumerate([str(name) for name in sorted_folders]):
        indiv_folder = os.path.join(images_path, folder)
        save_path = os.path.join(save_folder, f'{i}.jpg')

        if len(os.listdir(indiv_folder)) == 0:
            add_text_to_image(sentences[i], save_path)
        else:
            img_path = os.path.join(indiv_folder, os.listdir(indiv_folder)[0])
            add_text_to_image(sentences[i], save_path, img_path)

        save_paths.append(save_path)
    return save_paths

def make_output_folder():
    output_folder = os.path.join(os.getcwd(), 'output')
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)


# ------------ METHODS ABOVE ---------------- #

sentences = handle_audio_file(audio_file)
clear_corrupted_images("images")
save_paths = add_text_to_images(sentences)

save_gif(save_paths, "output/output.gif")

clear_images()