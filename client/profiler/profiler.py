
from tkinter import Tk, ttk, Text, StringVar, messagebox
import tkinter as tk
import tweepy as tw


class Profiler:

    def __init__(self):
        super().__init__()

    def get_user_profile(self, id=None, username=None):
        if not (id or username):
            raise ValueError(f"Please specify either the Twitter ID or Username of the user you would like to profile.")

