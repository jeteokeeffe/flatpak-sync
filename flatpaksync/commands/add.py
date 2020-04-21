import logging
import os

from flatpaksync.flatpakcmd import flatpakcmd
from flatpaksync.commands.command import command
from flatpaksync.configs.writeconfig import writeconfig
from flatpaksync.configs.readconfig import readconfig

from flatpaksync.app import app

class add(command):

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

                # Don't add Base Apps
            if appid.endswith("BaseApp"):
                logging.warn("unnecessary to add base apps")
            else:
                addApp=app(appid, repo)
                applist.add(addApp)

                    # Write configuration
                wconfig = writeconfig(conf)
                wconfig.setSettings(settings)
                wconfig.setRepoList(repolist)
                wconfig.setAppList(applist)

                if wconfig.write():
                    logging.info('successfully wrote configuration')
                else:
                    logging.error('failed to write configuration')

        else:
            logging.error('failed to read configuration')

