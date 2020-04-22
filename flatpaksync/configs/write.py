import json
import os
import logging

from flatpaksync.structs.applist import applist
from flatpaksync.structs.app import app
from flatpaksync.structs.repolist import repolist
from flatpaksync.structs.repo import repo
from flatpaksync.structs.settings import settings

mylog = logging.getLogger("fps")

class write:
    """
    Create a flatpak configuration file to save settings
    """

    def __init__(self, config = ""):
        self.config = config
        self.settings = settings()
        self.repolist = repolist()
        self.applist = applist()


    def setSettings(self, settings: settings) -> None:
        self.settings = settings


    def setAppList(self, applist: applist) -> None:
        self.applist = applist


    def setRepoList(self, repolist: repolist) -> None:
        self.repolist = repolist


    def write(self):

            # Global Settings
        settingsyaml = { 'remove_unmanaged_repos': self.settings.getRemoveUnmanagedRepos(),
            'remove_unmanaged_apps': self.settings.getRemoveUnmanagedApps() }

            # Set Repository 
        repoyaml = []
        for repo in self.repolist.getAll():
            repodata = { 'name':  repo.getName(),
                'repo':  repo.getLocation() }
            repoyaml.append(repodata)

            # Applications
        appyaml = []
        for app in self.applist.getAll():
            version = app.getVersion() if app.isMasked() else 'latest'
            appdata = { 'name':  app.getAppId(),
                'repo': app.getRepoName(),
                'version': version,
                'pin': app.isMasked() }

                # Set Application Permissions
            permlist = app.getPermissions()
            if permlist.getCount() > 0:
                perms = []
                for perm in permlist.getAll():
                    permstr="{}={}".format( perm.getPermission(), perm.getValue())
                    perms.append(permstr)
                appdata['permissions'] = perms

            appyaml.append(appdata)

            # Create Full data structure
        data = { 
            'sync': {
                'flatpak': 
                { 
                    'settings': settingsyaml,
                    'repos': repoyaml,
                    'apps' : appyaml 
                } 
            }
        }

            # Check if path is writable
        os.path.exists(self.config)

            # Check if writable
        os.access(self.config, os.W_OK) 

            # Open as writable
        try:
            with open(self.config, 'w') as f:
                json.dump(data, f, indent=4)
                #result = yaml.dump(data, f)
        except IOError as e:
            mylog.error("Failed to write configuration file")
            return False

        return True



