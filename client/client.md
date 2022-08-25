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

* API Token: `apik`
* API Token Secret: `apiks`
* Access Token: `at`
* Access Token Secret: `ats`

3. In your project, set **OAuth 1.0a** to enabled.

4. In the start menu search bar, type in "environment variables" and click *Edit the system and environment variables*.

5. In the window that pops up, click *Environment Variables* at the bottom-right.

6. Add `apik`, `apiks`, `at`, and `ats` to **System** variables, **NOT** User variables

7. Open autothreader.py in a text editor. Towards the top where it says `user = `, change `complexor00` to your username. Make sure not to delete the quotation marks!

8. Run `[script_name].py`

