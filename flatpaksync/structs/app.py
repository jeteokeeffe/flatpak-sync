from flatpaksync.structs.permissionlist import permissionlist

class app:

    '''
    flatpak application
    '''
    def __init__(self, appId = '', repoName =''):
        self.appId = appId
        self.repoName = repoName
        self.version = "latest"
        self.mask = False
        self.permlist = permissionlist()

    def setAppId(self, appId: str) -> None:
        self.appId = appId

    def setRepoName(self, repoName: str) -> None:
        self.repoName = repoName

    def setVersion(self, version: str) -> None:
        self.version = version

    def setPermissions(self, permlist: permissionlist) -> None:
        self.permlist = permlist

    def setMask(self, version) -> None:
        self.version = version
        self.mask = True



    def getAppId(self) -> str:
        return self.appId

    def getRepoName(self) -> str:
        return self.repoName

    def getVersion(self) -> str:
        return self.version

    def getPermissions(self) -> permissionlist:
        return self.permlist

    def isMasked(self) -> bool:
        return self.mask
