import logging
import os


class command():

    def __init__(self):
        self.conf = ".config/flatpak-sync/flatpak.json"
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


