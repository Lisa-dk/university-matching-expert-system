import webbrowser
from tkinter import *


def open_browser(url):
    webbrowser.open_new_tab(url)


class HyperlinkManager:
    def __init__(self, text):
        self.text = text
        self.text.tag_config("hyper", foreground="blue", underline=1)
        self.text.tag_bind("hyper", "<Button-1>", self._click)
        self.links = None
        self.reset()

    def reset(self):
        self.links = {}

    def add(self, url):
        tag = "hyper-%d" % len(self.links)
        self.links[tag] = url
        return "hyper", tag

    def _click(self, event):
        for tag in self.text.tag_names(CURRENT):
            if tag[:6] == "hyper-":
                open_browser(self.links[tag])
                return
