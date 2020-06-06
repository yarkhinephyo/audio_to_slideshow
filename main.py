from audio_parser import get_text_from_audio
from text_processing import *
from utils import *
from flickr_scraper import get_urls
from image_edit import add_text_to_image, save_gif
from video import save_output_video
import os
import time

def handle_audio_file(audio_file):
    parsed_text, timestamps = get_text_from_audio(audio_file)
    cleaned_text = get_expressions_removed(parsed_text)
    pos_tags = get_pos_tags(cleaned_text)
    search_terms = get_search_terms(pos_tags)

    for pos, search_term in search_terms:
        get_urls(search_term, str(pos), n=3, download=True)

    return get_sentences(pos_tags, search_terms), timestamps

def add_text_to_images(sentences):
    save_paths = []

    save_folder = os.path.join(os.getcwd(), 'images', 'final')
    if not os.path.isdir(save_folder):
        os.mkdir(save_folder)
    images_path = os.path.join(os.getcwd(), 'images')

    # Sort the folders after converting to integers
    sorted_folders = sorted([int(name) for name in os.listdir(images_path) if name != 'final' and name != 'gif'])

    for i, folder in enumerate([str(name) for name in sorted_folders]):
        indiv_folder = os.path.join(images_path, folder)
        save_path = os.path.join(save_folder, f'{i}.jpg')

        if len(os.listdir(indiv_folder)) == 0:
            add_text_to_image(sentences[i], save_path)
        else:
            img_path = os.path.join(indiv_folder, os.listdir(indiv_folder)[0])
            add_text_to_image(sentences[i], save_path, img_path)

        save_paths.append(save_path)

    # Final black frame
    save_path = os.path.join(save_folder, '1000.jpg')
    add_text_to_image('X', save_path)
    save_paths.append(save_path)

    return save_paths

def make_required_folder(folder):
    if not os.path.isdir(folder):
        os.mkdir(folder)


DEBUG = False

# ------------ METHODS ABOVE ---------------- #
if not DEBUG:   
    navigate_up_directory(2)

wav_dir = os.path.join(os.getcwd(), "wav_files")
audio_file = os.path.join(os.getcwd(), "wav_files", os.listdir(wav_dir)[0])

sentences, timestamps = handle_audio_file(audio_file)
frame_durations = get_frame_durations(sentences, timestamps)

clear_corrupted_images("images")
save_paths = add_text_to_images(sentences)

make_required_folder(os.path.join("images", "gif"))
save_gif(save_paths, os.path.join("images", "gif", "output.gif"), [duration for sentence, duration in frame_durations] + [200])

make_required_folder("output")
save_output_video(os.path.join("images", "gif", "output.gif"), audio_file, os.path.join("output", "output.mp4"))

time.sleep(2)
try:
    clear_images()
except PermissionError:
    pass