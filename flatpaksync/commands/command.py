import logging
import os

from flatpaksync.flatpakcmd import flatpakcmd

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
            logging.debug("Verbose mode enabled")
        else:
            logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


    def setDryRun(self, isDryrun):
        self.dryrun = isDryrun


    def checkFlatpak(self):
        fp = flatpakcmd()
        if fp.isInstalled() == False:
            sys.exit("Unable to find flatpak! Are you sure flatpak is installed?")
            
        logging.debug("Flatpak installed: {}".format(fp.isInstalled()))
        logging.debug(fp.getVersion())
        logging.debug("Configuration file: {}".format(self.conf))


