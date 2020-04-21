import logging
import os

from flatpaksync.flatpakcmd import flatpakcmd
from flatpaksync.commands.command import command
from flatpaksync.configs.write import write as writeconfig

from flatpaksync.structs.app import app
from flatpaksync.structs.settings import settings
from flatpaksync.actions.app import app as appaction
from flatpaksync.parserepo import parserepo
from flatpaksync.parseapp import parseapp
from flatpaksync.actions.repo import repo as repoaction


class generate(command):

    def __init__(self):
        super().__init__()

    def execute(self):

        conf = os.environ['HOME'] + '/' + self.conf
        if conf == ".config/flatpak-sync/flatpak.json":
            confFile = os.environ['HOME'] + '/' + conf
            confPath = os.path.dirname(os.path.realpath(confFile)) 
            Path(confPath).mkdir(parents=True, exist_ok=True)

        fp=flatpakcmd()
        if fp.isInstalled() == False:
            sys.exit("Unable to find flatpak! Are you sure flatpak is installed?")

        logging.debug("Flatpak installed: {}".format(fp.isInstalled()))
        logging.debug(fp.getVersion())
        logging.debug("Configuration file: {}".format(conf))

        
        raction=repoaction() 
        output = raction.list()
        rparse=parserepo()
        rparse.parse(output)

        action=appaction() 
        output=action.list()
        parse=parseapp()

        if parse.parse(output):

            fpsettings = settings()
            applist = parse.getAppList()
            repolist = rparse.getRepoList()

                # Write configuration
            wconfig = writeconfig(conf)
            wconfig.setSettings(fpsettings)
            wconfig.setRepoList(repolist)
            wconfig.setAppList(applist)

            if wconfig.write():
                logging.info('Successfully wrote configuration')
            else:
                logging.error('Failed to write configuration')

        else:
            logging.echo('Failed to parse apps')
