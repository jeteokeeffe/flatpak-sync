from .app import app

class applist:

    '''
    Flatpak Application list
    '''
    def __init__(self):
        self.applist = []
        self.count = 0

    def getAll(self):
        return self.applist


    def get(self, name) -> app:
        return self.applist[name]


    def add(self, app: app) -> bool:
        self.applist.append(app)
        self.count += 1
        return True


    def remove(self, app: app) -> bool:
        for i, stored in enumerate(self.applist):
            if stored.getAppId() == app.getAppId() and stored.getRepoName() == app.getRepoName():
                self.applist.pop(i)

        return True

    def getCount(self) -> int:
        return self.count

