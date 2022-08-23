import math
import os
import time
from tkinter import Tk, ttk, Text, StringVar, messagebox
import tkinter as tk
import tweepy as tw

user = "complexor00"


class Autothreader:
    """
    Breaks up blocks of text into individual tweets, then sends them all out in quick succession.
    Works for up to 99 tweets in a thread. Please, just...don't do more than 99. I'm begging you.

    Designed by VA Hensel.
    """

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

        self.thread = "🧵"
        self.thread_count = len(f" {self.thread} 00/00")
        self.tweet_length = 280 - self.thread_count

    def break_up_and_tweet(self, text, button, tweet_field):
        """
        The main event
        """
        if len(text) == 0:
            messagebox.showinfo("Empty", "Cannot send an empty tweet. Sorry!")
            return
        button.configure(text="Please wait...")

        number_of_tweets = math.ceil(len(text) / self.tweet_length)  # Number of tweets in thread after accounting for
        if number_of_tweets == 1:
            root_tweet = self.client.create_tweet(text=text).data["id"]
        else:
            pt = f"{self.thread} %s/{number_of_tweets}"  # Counter
            text = text.split()  # Words

            output = []
            num = 1
            while text:
                next_part = pt % str(num)
                next_output = ""
                while text and len(next_output) < self.tweet_length:
                    next_word = text[0]
                    if len(next_output) + len(next_word) < self.tweet_length:
                        next_output += " " + text.pop(0)
                    else:
                        break
                output.append(next_output + f" {next_part}")
                num += 1

            prev_tweet = self.client.create_tweet(text=output[0])
            root_tweet = prev_tweet.data["id"]
            print(prev_tweet.__repr__)
            for i in range(1, len(output)):
                prev_tweet = self.client.create_tweet(in_reply_to_tweet_id=prev_tweet.data["id"], text=output[i])
                print(prev_tweet.__repr__)
                time.sleep(2)
        button.configure(text="Send thread")
        tweet_field.delete("1.0", "end-1c")
        tweet_field.insert(tk.END, f"https://twitter.com/{user}/status/{root_tweet}")
        messagebox.showinfo("Success", "Thread successfully posted")


def main():
    at = Autothreader()

    # Build tkinter window
    root = Tk()
    root.title("Tweepy Autothreader")

    t = Text(root, height=25, width=100, wrap="word")
    t2 = Text(root, height=1, width=62)
    b = ttk.Button(root, text="Send thread")
    b.configure(command=lambda: at.break_up_and_tweet(t.get("1.0", "end-1c"), b, t2))
    l = ttk.Label(root, text="0 characters / 0 tweets")
    t.pack()
    b.pack()
    l.pack()
    t2.pack()

    def update_label(*args):
        num_chars = len(t.get("1.0", "end-1c"))
        l.config(text=f"{num_chars} characters / {int(math.ceil(num_chars / at.tweet_length))} tweets")

    root.bind("<Key>", update_label)

    root.mainloop()


if __name__ == "__main__":
    main()
