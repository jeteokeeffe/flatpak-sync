import logging
import os
from pathlib import Path

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

        if self.conf.endswith(".config/flatpak-sync/flatpak.json"):
            confPath = os.path.dirname(os.path.realpath(self.conf)) 
            Path(confPath).mkdir(parents=True, exist_ok=True)

        
        raction=repoaction() 
        output = raction.list()
        rparse=parserepo()
        rparse.parse(output)

        action = appaction() 
        output = action.list()
        parse = parseapp()

        if parse.parse(output):

            fpsettings = settings()
            applist = parse.getAppList()
            repolist = rparse.getRepoList()

                # Write configuration
            wconfig = writeconfig(self.conf)
            wconfig.setSettings(fpsettings)
            wconfig.setRepoList(repolist)
            wconfig.setAppList(applist)

            if wconfig.write():
                logging.info('Successfully wrote configuration')
            else:
                logging.error('Failed to write configuration')

        else:
            logging.echo('Failed to parse apps')
