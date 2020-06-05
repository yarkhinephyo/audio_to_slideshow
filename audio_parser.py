import os
import json 
from os.path import join, dirname 
from ibm_watson import SpeechToTextV1 
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import IAM_AUTHENTICATOR, IBM_URL


authenticator = IAMAuthenticator(IAM_AUTHENTICATOR)  
service = SpeechToTextV1(authenticator = authenticator)  
service.set_service_url(IBM_URL) 

def get_text_from_audio(audio_file):
    with open(audio_file, 'rb') as f: 
        dic = json.loads(json.dumps(service.recognize(audio=f, content_type='audio/wav', model='en-US_NarrowbandModel', continuous=True, timestamps=True,).get_result(), indent=2)) 
    
    transcript = ''
    for item in dic.get('results'):
        transcript += ' ' + item['alternatives'][0]['transcript']
        
    return transcript
