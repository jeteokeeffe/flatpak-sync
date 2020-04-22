import logging

from flatpaksync.commands.command import command
from flatpaksync.configs.write import write as writeconfig
from flatpaksync.configs.read import read as readconfig

from flatpaksync.structs.app import app

mylog = logging.getLogger("fps")

class remove(command):


    def __init__(self):
        super().__init__()


    def execute(self, repo, appid):
        
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
                    mylog.info('Successfully wrote configuration')
                else:
                    mylog.error('Failed to write configuration')
            else:
                mylog.warn("Unable to find application/repo {}".format(appid))

        else:
            mylog.error('Failed to read configuration')

