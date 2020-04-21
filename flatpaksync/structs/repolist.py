from flatpaksync.structs.repo import repo


class repolist:

    """
    Flatpak Repository list
    """
    def __init__(self):
        self.repolist = []
        self.count = 0


    def getAll(self):
        return self.repolist 


    def get(self, name) -> repo:
        return self.repolist[name]


    def getCount(self) -> int:
        return self.count
    

    def add(self, repo: repo) -> bool:
        self.repolist.append(repo)
        self.count += 1
        return True


    def exists(self, repo: repo) -> bool:
        return False

