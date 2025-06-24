import json
import os
import platform

class Config():
    '''Reptangles configuration class.'''
    def __init__(self):
        self.board = {}
        self.game = {}
        self.player = []
        self.scroll_speed = 10
        self.fullscreen = False

    def config_path(self):
        if platform.system() == "Linux":
            return os.path.expanduser("~/.config/reptangles/reptangles.json")
        elif platform.system() == "Windows":
            return os.path.join(os.getenv("APPDATA"), "reptangles", "reptangles.json")
        elif platform.system() == "Darwin":
            return os.path.expanduser("~/Library/Application Support/reptangles/reptangles.json")
        else:
            return "reptangles.json"

    def load(self):
        path = self.config_path()
        if os.path.exists(path):
            with open(path, "r") as f:
                data = json.load(f)
                self.__dict__.update(data)

    def save(self):
        path = self.config_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(self.__dict__, f, indent=2)

