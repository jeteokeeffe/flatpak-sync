import logging

from flatpaksync.flatpakcmd import flatpakcmd
from flatpaksync.commands.command import command
from flatpaksync.configs.write import write as writeconfig
from flatpaksync.configs.read import read as readconfig

from flatpaksync.structs.app import app


class remove(command):


    def __init__(self):
        super().__init__()


    def execute(self, repo, appid):

        fp=flatpakcmd()
        logging.debug("Flatpak installed: {}".format(fp.isInstalled()))
        logging.debug(fp.getVersion())
        logging.debug("Configuration file: {}".format(self.conf))

        
        config=readconfig(self.conf)
        if config.read():

            settings=config.getSettings()
            repolist=config.getRepoList()
            applist=config.getAppList()

                # Remove an App from the list
            removeApp = app(appid, repo)
            if applist.exists(removeApp):
                applist.remove(removeApp)

                    # Write configuration
                wconfig = writeconfig(self.conf)
                wconfig.setSettings(settings)
                wconfig.setRepoList(repolist)
                wconfig.setAppList(applist)

                if wconfig.write():
                    logging.info('Successfully wrote configuration')
                else:
                    logging.error('Failed to write configuration')
            else:
                logging.warn("Unable to find application/repo {}".format(appid))

        else:
            logging.error('Failed to read configuration')

