import subprocess


class flatpakcmd:
    """
    """

    def __init__(self):
        cmd = "flatpak --version"
        result = subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            self.installed = True
            self.version = result.stdout.strip()
            self.path = ""
        else:
            self.installed = False
            self.version = "N/A"
            self.path = ""


    def isInstalled(self):
        return self.installed


    def getVersion(self):
        return self.version


    def getPath(self):
        return self.path

    


