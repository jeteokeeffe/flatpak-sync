import logging
import os


class command():

    def __init__(self):
        self.dryrun = False

        self.conf = os.environ['HOME'] + '/' + ".config/flatpak-sync/flatpak.json"


    def setConfig(self, conf):
        if not conf.endswith(".config/flatpak-sync/flatpak.json"):
            self.conf = conf


    def setDebug(self, isVerbose):
        if isVerbose:
            logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
        else:
            logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


    def setDryRun(self, isDryrun):
        self.dryrun = isDryrun




