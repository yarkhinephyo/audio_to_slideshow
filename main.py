from audio_parser import get_text_from_audio
from text_processing import *
from utils import *
from flickr_scraper import get_urls
from image_edit import add_text_to_images, save_gif
from video import save_output_video
import os
import time

def handle_audio_file(audio_file):
    parsed_text, timestamps = get_text_from_audio(audio_file)
    cleaned_text = get_expressions_removed(parsed_text)
    pos_tags = get_pos_tags(cleaned_text)
    search_terms = get_search_terms(pos_tags)

    for pos, search_term in search_terms:
        get_urls(search_term, str(pos), n=3)

    return get_sentences(pos_tags, search_terms), timestamps

def make_required_folder(folder):
    if not os.path.isdir(folder):
        os.mkdir(folder)


DEBUG = True

# ------------ METHODS ABOVE ---------------- #
if not DEBUG:   
    navigate_up_directory(2)

wav_dir = os.path.join(os.getcwd(), "wav_files")
audio_file = os.path.join(os.getcwd(), "wav_files", os.listdir(wav_dir)[0])

sentences, timestamps = handle_audio_file(audio_file)
frame_durations = get_frame_durations(sentences, timestamps)

clear_corrupted_images("images")
save_paths = add_text_to_images(sentences, os.path.join(os.getcwd(), 'images', 'final'), os.path.join(os.getcwd(), 'images'))

make_required_folder(os.path.join("images", "gif"))
save_gif(save_paths, os.path.join("images", "gif", "output.gif"), [duration for sentence, duration in frame_durations] + [200])

make_required_folder("output")
save_output_video(os.path.join("images", "gif", "output.gif"), audio_file, os.path.join("output", "output.mp4"))

time.sleep(2)
try:
    clear_images()
except PermissionError:
    pass