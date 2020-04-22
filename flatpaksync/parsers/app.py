import logging

from flatpaksync.structs.applist import applist
from flatpaksync.structs.app import app as appdata
from flatpaksync.actions.permission import permission as permissionaction
from flatpaksync.parsers.permission import permission as parsepermission

class app:

    """
    parse output of flatpak list
    """
    def __init__(self):
        self.appList = applist()


    def parse(self, output: str):
        appid = 0
        version = 1
        repo = 2

        for line in output.splitlines():
            cols=line.split("\t")

                # Create App & Settings
            if not cols[appid].endswith(".BaseApp"):
                myapp = appdata()
                myapp.setAppId(cols[appid])
                myapp.setVersion(cols[version])
                myapp.setRepoName(cols[repo])

                    # Check for override permissions
                permaction = permissionaction() 
                output = permaction.list(myapp)
                permparse = parsepermission()
                permparse.parse(output)
                permlist = permparse.getPermissions()
                #if permlist.getCount() > 0:
                    #for permobj in permlist.getAll():
                myapp.setPermissions(permlist)

                    # Add App
                self.appList.add(myapp)
            else:
                logging.debug("Ignoring {}".format(cols[appid]))

        return True


    def getAppList(self):
        return self.appList
