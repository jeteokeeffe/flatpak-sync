import json
import os.path
import logging

from flatpaksync.structs.applist import applist
from flatpaksync.structs.app import app
from flatpaksync.structs.repolist import repolist
from flatpaksync.structs.repo import repo
from flatpaksync.structs.permissionlist import permissionlist
from flatpaksync.structs.permission import permission
from flatpaksync.structs.settings import settings

mylog = logging.getLogger("fps")

class read:
    """ 
    Read flatpak configuration file to load settings
    """

    def __init__(self, config: str = ""):
        self.config = config
        self.settings = settings()
        self.appList = applist()
        self.repoList = repolist()
        self.error = ""


    def read(self):

            # Check if path is readable
        #os.path.exists()

            # Check if file exists
        #os.path.isfilea(self.config)

            # Check if file is readable
        #os.access(self.config, os.R_OK) = true

            # Open file
        with open(self.config) as f:
            parsed = json.load(f)

            if not parsed['sync']['flatpak']:
                mylog.error("Bad format or missing flatpak applications")
                return False

            root = parsed['sync']['flatpak'] 

                # Load global settings
            if 'settings' in root:
                if 'remove_unmanaged_repos' in root:
                    self.settings.setRemoveUnmanagedRepos(root['settings']['remove_unmanaged_repos'])

                if 'remove_unmanaged_apps' in root['settings']:
                    self.settings.setRemoveUnmanagedRepos(root['settings']['remove_unmanaged_apps'])
            else:
                mylog.error('unable to find settings')
                return False


                # Load Repository settings
            if 'repos' in root:
                for configrepo in root['repos']:
                    self.repoList.add( repo(configrepo['name'],configrepo['repo']) )
            else:
                mylog.error('failed to find repos')
                return False

                # Load Application settings
            if 'apps' in root:
                for configapp in root['apps']:
                    myapp = app(configapp['name'], configapp['repo'])
                    #myapp.setVersion()

                        # Add Permissions
                    if 'permissions' in configapp:
                        permlistobj = permissionlist()

                            # Loop thru permissions
                        for i in configapp['permissions']:
                            permlistobj.add(permission(i))

                        myapp.setPermissions(permlistobj)

                    self.appList.add(myapp)
            else:
                mylog.error('failed to find apps')
                return False

        return True

            

    def getSettings(self) -> settings:
        return self.settings

    def getRepoList(self) -> repolist:
        return self.repoList

    def getAppList(self) -> applist:
        return self.appList


    def getError(self) -> str:
        return self.error
