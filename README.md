
# Audio To Slideshow 

Automatically converts :speech_balloon: speech in an audio file into a :video_camera: video with accompanying relevant images.
Medium: https://medium.com/@yarkhinephyo/hey-python-make-me-a-video-e7be78590b8d

## Usage
Ensure you have subscribed to IBM Watson's Speech to Text service and Flickr API.
```
cd ./audio_to_slideshow
echo '
IAM_AUTHENTICATOR={ibm_iam_authenticator}
IBM_URL={speech_to_text_watson_instance_url}
FLICKR_KEY={flickr_key}
FLICKR_SECRET={flickr_secret}
' > .env
```

#### Method 1: Dockerfile

Ensure Docker engine is running
```
docker build -t audio_to_images:1.0 .

# Ensure .mp3 file exists at /path/to/input/dir
docker run --rm --env-file ./.env -v /path/to/input/dir:/app/input -v /path/to/output/dir:/app/output audio_to_images:1.0

# The output video file will be at /path/to/output/dir
```
#### Method 2: Pipfile

Ensure Pipenv is installed
```
pipenv install
pipenv shell
cd ./app
mkdir input output

# Ensure .mp3 file exists at ./app/input

pipenv run python main.py
```
## Sample Output Video
[![IMAGE ALT TEXT](http://img.youtube.com/vi/j8BddvXT9d0/0.jpg)](http://www.youtube.com/watch?v=j8BddvXT9d0 "Sample Output Video")

## Acknowledgements

- Inspired by youtuber Carykh.
- Flickr scraper by Ultralytics LLC.
- Text to speech API by IBM