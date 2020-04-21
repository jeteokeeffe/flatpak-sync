import logging
import os

from flatpaksync.flatpakcmd import flatpakcmd
from flatpaksync.commands.command import command
from flatpaksync.configs.readconfig import readconfig

from flatpaksync.app import app
from flatpaksync.appaction import appaction
from flatpaksync.permissionaction import permissionaction

class run(command):

    def __init__(self):
        super().__init__()

    def execute(self):

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

                # Install Applications
            for app in applist.getAll():
                action=appaction()
                permaction=permissionaction()

                if action.isInstalled(app):
                    logging.debug('{} already installed'.format(app.getAppId()))
                else:
                    if dryrun:
                        logging.info('{} to be installed'.format(app.getAppId()))
                    elif action.install(app):
                        logging.info('{} installation successful'.format(app.getAppId()))
                    else:
                        logging.error('{} installation failed'.format(app.getAppId()))

                perms = app.getPermissions()
                if perms.getCount() > 0:
                    logging.debug('{} has overriding permissions'.format(app.getAppId()))
                    for permission in perms.getAll():
                        if permaction.override(app, permission):
                            logging.debug(" permission set")
                        else:
                            logging.error("{} failed to set permission '{}'".format(app.getAppId(), permission.getPermission()))

                #else
                #    logging.debug('{} has no overriding permissions'.format(app.getAppId()))
        else:
            logging.info('failed to read configuration')
