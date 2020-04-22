import subprocess

from flatpaksync.structs.repo import repo
from flatpaksync.parsers.repo import repo as parserepo

class repo:

    def __init__(self):
        self.type = "user"

    def add(self, repo: repo) -> bool:
        cmd = "flatpak remote-add --if-not-exists --{} {} {} ".format(self.type, repo.getName(), repo.getLocation())
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #print(result.stdout)
        #print(result.stderr)
        if result.returncode == 0:
            return True
        else:
            return False


    def remove(self, repo: repo) -> bool:
        cmd = "flatpak remote-delete {}".format(repo.getName())
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #print(result.stdout)
        #print(result.stderr)
        if result.returncode == 0:
            return True
        else:
            return False


    def isInstalled(self, repo: repo) -> bool:
        cmd = "flatpak remotes | grep -c {}".format(repo.getName())
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            if int(result.stdout.strip()) > 0:
                return True

        return False


    def list(self) -> str:
        cmd = "flatpak remotes --columns=name,url"
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout



