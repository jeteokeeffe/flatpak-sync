import yaml
import os.path

from .applist import applist
from .app import app
from .repolist import repolist
from .repo import repo
from .permissionlist import permissionlist
from .permission import permission
from .settings import settings


class readconfig:
    """ 
    Read flatpak configuration file to load settings
    """

    def __init__(self, config: str = ""):
        self.config = config
        self.settings = settings()
        self.appList = applist()
        self.repoList = repolist()
        self.error = ""

    def validate(self) -> bool:
            # Check if file contents are in proper yaml
        return True


    def read(self):

            # Check if path is readable
        #os.path.exists()

            # Check if file exists
        #os.path.isfilea(self.config)

            # Check if file is readable
        #os.access(self.config, os.R_OK) = true

            # Open file
        with open(self.config) as f:
            data = yaml.load_all(f, Loader=yaml.FullLoader)
            for flatpak in data:
                root = flatpak['sync']['flatpak'] 

                    # Load global settings
                if 'settings' in root:
                    if 'remove_unmanaged_repos' in root:
                        self.settings.setRemoveUnmanagedRepos(root['settings']['remove_unmanaged_repos'])

                    if 'remove_unmanaged_apps' in root['settings']:
                        self.settings.setRemoveUnmanagedRepos(root['settings']['remove_unmanaged_apps'])
                else:
                    print('unable to find settings')
                    return False


                    # Load Repository settings
                if 'repos' in root:
                    for configrepo in root['repos']:
                        self.repoList.add( repo(configrepo['name'],configrepo['repo']) )
                else:
                    print('failed to find repos')
                    return False

                    # Load Application settings
                if 'apps' in root:
                    for configapp in root['apps']:
                        myapp = app(configapp['name'], configapp['repo'])
                        #myapp.setVersion()

                            # Add Permissions
                        if 'permissions' in configapp:
                            print('Found permissions')
                            permlistobj = permissionlist()
                            #permlistobj->add(permission(name, val))
                            #myapp->setPermissions(permlistobj)

                        self.appList.add(myapp)
                else:
                    print('failed to find apps')
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
