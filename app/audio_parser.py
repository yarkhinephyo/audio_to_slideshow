import os
import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import IAM_AUTHENTICATOR, IBM_URL
import mimetypes

authenticator = IAMAuthenticator(IAM_AUTHENTICATOR)
service = SpeechToTextV1(authenticator=authenticator)
service.set_service_url(IBM_URL)


def get_text_from_audio(audio_file):
    """Retrieves transcript and timestamps of words from an audio file

    Args:
        audio_file (str): Path to audio file

    Returns:
        [tuple]: (
            transcript_string,
            [
                [<word_string>, <start_time_float>, <end_time_float> ],
                ...
            ]
        )
    """
    mime_type = mimetypes.guess_type(audio_file)[0]
    assert mime_type.split("/")[0] == 'audio'

    with open(audio_file, 'rb') as f:
        dic = json.loads(json.dumps(service.recognize(audio=f, content_type=mime_type,
                         model='en-US_NarrowbandModel', continuous=True, timestamps=True,).get_result(), indent=2))

    transcript = ''
    timestamps = []
    for item in dic.get('results'):
        transcript += ' ' + item['alternatives'][0]['transcript']
        timestamps.extend(item['alternatives'][0]['timestamps'])

    return transcript, timestamps
