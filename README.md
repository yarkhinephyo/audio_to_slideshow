## audio_to_slideshow

Automatically converts a speech in an audio file into a video with accompanying relevant images

### Instructions
- Add a config.py to the root folder
  - Set IAM_AUTHENTICATOR <From IBM Speech to text API>, IBM_URL, FLICKR_KEY <From Flickr image API>, FLICKR_SECRET
  - Set WIDTH, HEIGHT <Dimensions of output video>
- Place an audio file of a speech <.wav> in the wav_files directory
- Run main.py
- The output video <.mp4> will be produced
  
### Sample output video
- https://youtu.be/j8BddvXT9d0

### Acknowledgements
- Inspired by youtuber Carykh.
- Flickr scraper by Ultralytics LLC.
- Text to speech API by IBM
