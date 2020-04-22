import subprocess

from flatpaksync.structs.app import app
from flatpaksync.parsers.app import app as parseapp


class app:
    """
    flatpak application commands like install an app, remove an app
    """

    def install(self, app: app) -> bool:
        cmd = "flatpak install --assumeyes --noninteractive {} {}".format(app.getRepoName(), app.getAppId())
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return True
        else:
            return False


    def remove(self, app: app) -> bool:
        cmd = "flatpak remove --assumeyes --noninteractive {}".format(app.getAppId())
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return True
        else:
            return False


    def isInstalled(self, app: app) -> bool:
        cmd = "flatpak list | grep -c {}".format(app.getAppId())
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if int(result.stdout.strip()) > 0:
            return True
        else:
            return False


    def mask(self, app: app) -> bool:
        cmd = "flatpak mask {}".format(app.getAppId())
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True


    def unmask(self, app: app) -> bool:
        cmd = "flatpak unmask {}".format(app.getAppId())
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True


    def list(self) -> str:
        cmd = "flatpak list --app --columns=application,version,origin"
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout


