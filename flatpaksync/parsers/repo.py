from flatpaksync.structs.repolist import repolist
from flatpaksync.structs.repo import repo as repodata


class repo:

    """
    Parse flatpak output
    """
    def __init__(self):
        self.repoList = repolist()


    def parse(self, output: str):
        name = 0
        location = 1

        for line in output.splitlines():
            cols = line.split("\t")

            myrepo = repodata(cols[name])
            myrepo.setLocation(repodata.nameToLocation(cols[name]))
            self.repoList.add(myrepo)

        return True

    def getRepoList(self):
        return self.repoList

