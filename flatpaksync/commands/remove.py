import logging
import os

from flatpaksync.flatpakcmd import flatpakcmd
from flatpaksync.commands.command import command
from flatpaksync.configs.writeconfig import writeconfig
from flatpaksync.configs.readconfig import readconfig

from flatpaksync.app import app


class remove(command):

    def __init__(self):
        super().__init__()

    def execute(self, repo, appid):

        conf = os.environ['HOME'] + '/' + self.conf


        fp=flatpakcmd()
        logging.debug("Flatpak installed: {}".format(fp.isInstalled()))
        logging.debug(fp.getVersion())
        logging.debug("Configuration file: {}".format(conf))

        
        config=readconfig(conf)
        if config.read():

            settings=config.getSettings()
            repolist=config.getRepoList()
            applist=config.getAppList()

                # Remove an App from the list
            removeApp=app(appid, repo)
            applist.remove(removeApp)

                # Write configuration
            wconfig = writeconfig(conf)
            wconfig.setSettings(settings)
            wconfig.setRepoList(repolist)
            wconfig.setAppList(applist)

            if wconfig.write():
                logging.info('Successfully wrote configuration')
            else:
                logging.error('Failed to write configuration')

        else:
            logging.error('Failed to read configuration')

