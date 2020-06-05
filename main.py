from audio_parser import get_text_from_audio
from utils import *
from flickr_scraper import get_urls
import os

# audio_file = os.path.join("wav_files", "audio_1.wav")

def handle_audio_file(audio_file):
    parsed_text = get_text_from_audio(audio_file)
    cleaned_text = get_expressions_removed(parsed_text)
    search_terms = get_search_terms(get_pos_tags(cleaned_text))

    for pos, search_term in search_terms:
        get_urls(search_term, str(pos), n=3, download=True)

# handle_audio_file(audio_file)

clear_corrupted_images("images")

# clear_images()