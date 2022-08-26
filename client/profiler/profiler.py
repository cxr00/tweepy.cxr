import sys; sys.path.append("../")

from client import Client

from datetime import datetime
import json
import os

from tkinter import Tk, ttk, Text, StringVar, messagebox
import tkinter as tk

import tweepy as tw


class Profiler(Client):

    """
    Use the v1.1 API to assemble a record of a user's profile.

    Consider this an excellent primer on the data structure associated with the get_user method
    """

    def __init__(self):
        super().__init__()
        self.profile = {}

    def get_user_profile(self, user_id=None, screen_name=None, **kwargs):
        if not (user_id or screen_name):
            raise ValueError(f"Please specify either the Twitter ID or Username of the user you would like to profile.")

        # Get basic
        user = self.api.get_user(user_id=user_id, screen_name=screen_name, **kwargs)

        self.profile = user._json  # For saving
        if not (self.profile["suspended"] or self.profile["protected"]):
            self.profile.update({"user_timeline": list([u._json for u in list(user.timeline(count=50, trim_user=True))])})
        else:
            print(f"User is {'suspended' if self.profile['suspended'] else 'protected'}.")

    def save(self, save_dir="./{}"):
        save_dir = save_dir.format(self.profile["id"])
        if not os.path.isdir(save_dir):
            os.mkdir(save_dir.format())
        with open(save_dir + "/" + str(datetime.now())[:10] + ".txt", "w+") as f:
            f.write(json.dumps(self.profile, indent=4))

    def presentation(self):
        if not self.profile:
            return ""

        if self.profile["suspended"] or self.profile["protected"]:
            return f"This user is {'suspended' if self.profile['suspended'] else 'protected'}"

        name = self.profile["name"]
        screen_name = self.profile["screen_name"]
        location = self.profile["location"]
        description = self.profile["description"]
        url = self.profile["entities"]["url"]["urls"][0]["expanded_url"]
        followers_count = self.profile["followers_count"]
        friends_count = self.profile["friends_count"]
        created_at = self.profile["created_at"]
        statuses_count = self.profile["statuses_count"]
        profile_image_url = self.profile["profile_image_url"]
        profile_banner_url = self.profile["profile_banner_url"]
        withheld_in_countries = self.profile["withheld_in_countries"]

        s = [
            f"name: {name} (@{screen_name})",
            location,
            "",
            f"Has posted {statuses_count} statuses since creation at {created_at}",
            f"description: {description}",
            f"url: {url}",
            "",
            f"{friends_count} following / {followers_count} followers",
            "",
            f"Withheld in {', '.join(withheld_in_countries)}" if withheld_in_countries else "",
            f"Profile picture: {profile_image_url}",
            f"Profile banner: {profile_banner_url}"
        ]
        return "\n".join(s)

    def timeline(self):
        return "\n".join([f"{tweet['created_at']} - {tweet['text']}" for tweet in self.profile['user_timeline']])


p = Profiler()
p.get_user_profile(screen_name="complexor00")
p.save()
print(p.presentation())
print()
print(p.timeline())
