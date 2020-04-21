import logging
import os


class command():

    def __init__(self):
        self.conf = os.environ['HOME'] + '/' + ".config/flatpak-sync/flatpak.json"
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


    def setConfig(self, conf):
        self.conf = conf


    def setLogLevel(self, level):
        self.logLevel = level




