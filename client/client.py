
import os
import tweepy as tw


class Client:

    def __init__(self):
        apik = os.environ.get("apik")
        apiks = os.environ.get("apiks")
        at = os.environ.get("at")
        ats = os.environ.get("ats")

        self.client = tw.Client(
            consumer_key=apik,
            consumer_secret=apiks,
            access_token=at,
            access_token_secret=ats
        )
