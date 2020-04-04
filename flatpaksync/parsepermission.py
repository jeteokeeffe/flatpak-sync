import configparser
import io

from .permission import permission
from .permissionlist import permissionlist

class parsepermission:

    def __init__(self):
        self.permlist = permissionlist()

    def parse(self, output: str):
        buf = io.StringIO(output)
        config = configparser.ConfigParser()
        config.read_file(buf)
        for section in config.sections():
            for permname in config[section]:
                for val in config[section][permname].split(';'):
                    if len(val) > 0:
                        perm = permission(permname, val)
                        self.permlist.add(perm)


    def getPermissions(self):
        return self.permlist

    def safetype(self, permname: str):
        """
        List of permissions
        'share':
        'unshare':
        'socket':
        'nosocket':
        'device':
        'nodevice':
        'allow':
        'disallow':
        'filesystem':
        'nofilesystem':
        'add-policy':
        'remove-policy':
        'env':
        'own-name':
        'talk-name':
        'no-talk-name':
        'system-own-name':
        'system-talk-name':
        'system-no-talk-name':
        'persist':
        """

        options = {
            'filesystems': 'filesystem',
            'filesystem': 'filesystem',
            'sockets': 'socket',
            'persist': 'persist',
            'env': 'env',
            'persist': 'persist',
        }

        return options.get(permname, 'invalid');


#name="filesystemss"
#p=parsepermission()
#print(p.safetype(name))
