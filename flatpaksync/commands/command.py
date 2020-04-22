import logging
import os

from flatpaksync.flatpakcmd import flatpakcmd

mylog = logging.getLogger("fps")

class command():

    def __init__(self):
        self.dryrun = False

        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

        self.conf = os.environ['HOME'] + '/' + ".config/flatpak-sync/flatpak.json"


    def setConfig(self, conf):
        if not conf.endswith(".config/flatpak-sync/flatpak.json"):
            self.conf = conf


    def setDebug(self, isVerbose):
        if isVerbose:
            mylog.setLevel(logging.DEBUG)
            mylog.debug("Verbose mode enabled")
        else:
            mylog.setLevel(logging.INFO)


    def setDryRun(self, isDryrun):
        self.dryrun = isDryrun


    def checkFlatpak(self):
        fp = flatpakcmd()
        if fp.isInstalled() == False:
            sys.exit("Unable to find flatpak! Are you sure flatpak is installed?")
            
        mylog.debug("Flatpak installed: {}".format(fp.isInstalled()))
        mylog.debug(fp.getVersion())
        mylog.debug("Configuration file: {}".format(self.conf))


