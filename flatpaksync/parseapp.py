from .applist import applist
from .app import app 
from .permissionaction import permissionaction
from .parsepermission import parsepermission

class parseapp:

    """
    parse output of flatpak list
    """
    def __init__(self):
        self.appList = applist()


    def parse(self, output: str):
        appid = 0
        version = 1
        repo = 2

        #print(output)
        for line in output.splitlines():
            cols=line.split("\t")

                # Create App
            myapp = app()
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

            self.appList.add(myapp)

        return True


    def getAppList(self):
        return self.appList
