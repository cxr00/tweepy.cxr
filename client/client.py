
import os
import tweepy as tw


class Client:

    """
    Access Twitter API v1.1 via self.api and v2 via self.client

    See client.md for info on setting up environment variables
    """

    def __init__(self):
        apik = os.environ.get("TWITTER_API_KEY")
        apiks = os.environ.get("TWITTER_API_KEY_SECRET")
        at = os.environ.get("TWITTER_ACCESS_TOKEN")
        ats = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

        self.client = tw.Client(
            consumer_key=apik,
            consumer_secret=apiks,
            access_token=at,
            access_token_secret=ats
        )

        self._auth = tw.OAuth1UserHandler(
            apik,
            apiks,
            at,
            ats
        )

        self.api = tw.API(self._auth)
