

class mask:
    """
    flatpak mask command
    """


    def mask(self):
        cmd = "flatpak mask {}".format(app.getAppId())
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return True
        else:
            return False

    def unmask(self):
        cmd = "flatpak mask --remove {}".format(app.getAppId())
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return True
        else:
            return False


    def ismasked(self):
        cmd = "flatpak mask"
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return True
        else:
            return False
