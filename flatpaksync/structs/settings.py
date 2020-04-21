

class settings:
    '''
    Global Flatpak settings
    '''

    def __init__(self):
        self.systemInstall = False
        self.removeUnmanagedRepos = False
        self.removeUnmanagedApps = False

    def setSystemInstallation(self, option: bool):
        self.systemInstall = option

    def setRemoveUnmanagedRepos(self, option: bool):
        self.removeUnmanagedRepos = option

    def setRemoveUnmanagedApps(self, option: bool):
        self.removeUnmanagedApps = option


    def getSystemInstallation(self) -> bool:
        return self.systemInstall

    def getRemoveUnmanagedRepos(self) -> bool:
        return self.removeUnmanagedRepos

    def getRemoveUnmanagedApps(self) -> bool:
        return self.removeUnmanagedApps
