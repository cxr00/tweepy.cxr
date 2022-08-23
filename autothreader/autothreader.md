## autothreader.autothreader

A simple tkinter application which takes a block of text and turns it into a tweet thread.

## Setup (Windows)

0a. Install Python (3.9.12 is the version I used to develop this)

0b. Open the console (type cmd in the start menu search bar) and use the following command:

```
pip install tweepy
```

1. Apply to use the Twitter API at https://developer.twitter.com/en.
2. Once your application is accepted, create a project and generate (and copy!) the following:

* API Token: `apik`
* API Token Secret: `apiks`
* Access Token: `at`
* Access Token Secret: `ats`

3. In your project, set **OAuth 1.0a** to enabled.

4. In the start menu search bar, type in "environment variables" and click *Edit the system and environment variables*.

5. In the window that pops up, click *Environment Variables* at the bottom-right.

6. Add `apik`, `apiks`, `at`, and `ats` to **System** variables, **NOT** User variables

7. Open autothreader.py in a text editor. Towards the top where it says `user = `, change `complexor00` to your username. Make sure not to delete the quotation marks!

8. Run `autothreader.py`

## Use

Type in the text you want to tweet. The label directly underneath the *Send tweet* button will tell you how many characters you've typed, as well as how many tweets it will take up. In the event that your text only constitutes a single tweet, it will be sent without the thread indicator.

After sending (a) tweet(s) the root tweet will be generated in the text field below the tracking label. You can use this to quickly navigate to your new thread.
