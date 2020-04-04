import subprocess

from .app import app
from .permission import permission

class permissionaction:
    """
    Flatpak permissions
    """

    def reset(self):
        cmd = "flatpak install --assumeyes --noninteractive {} {}".format(app.getRepoName(), app.getAppId())
        return True


    def override(self, myapp: app, myperm: permission):
        cmd = "flatpak override --user {} {}".format(myapp.getAppId(), myperm.toCmd())
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return result.stdout
        return False


    def list(self, myapp: app):
        cmd = "flatpak override --user --show {}".format(myapp.getAppId())
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return result.stdout
        return False


    def remove(self) -> bool:
        return True
