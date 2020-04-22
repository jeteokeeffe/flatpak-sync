import logging
import os
from pathlib import Path

from flatpaksync.commands.command import command
from flatpaksync.configs.write import write as writeconfig
from flatpaksync.configs.read import read as readconfig

from flatpaksync.structs.app import app

mylog = logging.getLogger("fps")

class add(command):

    def __init__(self):
        super().__init__()

    def execute(self, repo, appid):

        if self.conf.endswith(".config/flatpak-sync/flatpak.json"):
            confPath = os.path.dirname(os.path.realpath(self.conf)) 
            Path(confPath).mkdir(parents=True, exist_ok=True)

        config = readconfig(self.conf)
        if config.read():
            settings=config.getSettings()
            repolist=config.getRepoList()
            applist=config.getAppList()

                # Don't add Base Apps
            if appid.endswith(".BaseApp"):
                mylog.warn("Unnecessary to add base apps")
            else:
                addApp = app(appid, repo)
                applist.add(addApp)

                    # Write configuration
                wconfig = writeconfig(self.conf)
                wconfig.setSettings(settings)
                wconfig.setRepoList(repolist)
                wconfig.setAppList(applist)

                if wconfig.write():
                    mylog.info('Successfully wrote configuration')
                else:
                    mylog.error('Failed to write configuration')

        else:
            mylog.error('Failed to read configuration')

