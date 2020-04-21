

class permission:

    TYPE_USER = "user"
    TYPE_SYSTEM = "system"

    def __init__(self, line: str = ""):
        if not line == "":
            self.setPermission(line.split("=")[0], line.split("=")[1])
        self.type = "user"

    def setPermission(self, permission: str, val: str) -> bool:
        options = {
            'filesystems': 'filesystem',
            'filesystem': 'filesystem',
            'sockets': 'socket',
            'persist': 'persist',
            'env': 'env',
            'persist': 'persist',
        }

        self.permission = options.get(permission);
        self.value = val

        return True


    def getPermission(self) -> str:
        return self.permission

    def getValue(self) -> str:
        return self.value

    def toCmd(self) -> str:
        return "--{}={}".format(self.permission, self.value)


