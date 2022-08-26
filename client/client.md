## core.client.Client

A simple wrapper class used in `tweepy.cxr`.

## Setup (Windows)

0a. Install Python (3.9.12 is the version I used to develop this)

0b. Open the console (type cmd in the start menu search bar) and use the following command:

```
pip install tweepy
```

1. Apply to use the Twitter API at https://developer.twitter.com/en.


2. Once your application is accepted, create a project and generate (and copy!) the following:

* API Key: `TWITTER_API_KEY`
* API Key Secret: `TWITTER_API_KEY_SECRET`
* Access Token: `TWITTER_ACCESS_TOKEN`
* Access Token Secret: `TWITTER_ACCESS_TOKEN_SECRET`


3. In your project, set OAuth 1.0 AND 2.0 to enabled.


4. In the start menu search bar, type in "environment variables" and click *Edit the system and environment variables*.


5. In the window that pops up, click *Environment Variables* at the bottom-right.


6. Add those four values to **System** variables, **NOT** User variables. If the program fails to run, doublecheck you haven't misspelled anything! If it still doesn't work, go to the project in the Twitter Developer portal and "regenerate" those four values.


7. **If you are using the Autothreader:** Open autothreader.py in a text editor. Towards the top where it says `user = `, change `complexor00` to your username. Make sure not to delete the quotation marks!


8. Run whichever script you want to use!
