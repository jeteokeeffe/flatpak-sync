from flatpaksync.structs.permission import permission

class permissionlist():

    """
    list of flatpak permissions for a specific app
    """
    def __init__(self):
        self.permlist = []
        self.count = 0


    def getAll(self):
        return self.permlist 


    def get(self, name: str):
        return self.permlist[name]


    def getCount(self) -> int:
        return self.count
    

    def add(self, perm) -> bool:
        self.permlist.append(perm)
        self.count = self.count + 1
        return True


    def exists(self, perm: permission) -> bool:
        return False
