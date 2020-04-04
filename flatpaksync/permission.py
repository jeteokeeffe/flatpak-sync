

class permission:

    def __init__(self, permission: str = "", val: str = ""):
        self.permission = permission
        self.value = val
        self.type = "user"

    def setPermission(self, permission: str, val: str) -> bool:
        self.permission = permission
        self.value = val
        return True


    def getPermission(self) -> str:
        return self.permission

    def getValue(self) -> str:
        return self.value


    def toCmd(self) -> str:
        return "--{}={}".format(self.permission, self.value)
