import logging
import os

from flatpaksync.commands.command import command
from flatpaksync.configs.read import read as readconfig

from flatpaksync.structs.app import app
from flatpaksync.actions.app import app as appaction
from flatpaksync.actions.permission import permission as permissionaction

mylog = logging.getLogger("fps")

class run(command):

    def __init__(self):
        super().__init__()


    def execute(self):

        config = readconfig(self.conf)
        if config.read():
            settings=config.getSettings()
            repolist=config.getRepoList()
            applist=config.getAppList()

                # Install Applications
            for app in applist.getAll():
                action=appaction()
                permaction=permissionaction()

                if action.isInstalled(app):
                    mylog.debug('{} already installed'.format(app.getAppId()))
                else:
                    if self.dryrun:
                        mylog.info('{} to be installed'.format(app.getAppId()))
                    elif action.install(app):
                        mylog.info('{} installation successful'.format(app.getAppId()))
                    else:
                        mylog.error('{} installation failed'.format(app.getAppId()))

                perms = app.getPermissions()
                if perms.getCount() > 0:
                    mylog.debug('{} has overriding permissions'.format(app.getAppId()))
                    for permission in perms.getAll():
                        if permaction.override(app, permission):
                            mylog.debug(" permission set")
                        else:
                            mylog.error("{} failed to set permission '{}'".format(app.getAppId(), permission.getPermission()))

                #else
                #    mylog.debug('{} has no overriding permissions'.format(app.getAppId()))
        else:
            mylog.info('failed to read configuration')
