import os

IAM_AUTHENTICATOR = os.environ.get("IAM_AUTHENTICATOR")

IBM_URL = os.environ.get("IBM_URL")

FLICKR_KEY = os.environ.get("FLICKR_KEY") # https://www.flickr.com/services/apps/create/apply

FLICKR_SECRET = os.environ.get("FLICKR_SECRET") 

LICENSE_TYPES = os.environ.get("LICENSE_TYPES", default="1,2,3,4,5,6,7,8,9,10") # http://www.flickr.com/services/api/flickr.photos.search.html

WIDTH = int(os.environ.get("VIDEO_WIDTH", default=640))
HEIGHT = int(os.environ.get("VIDEO_HEIGHT", default=360))