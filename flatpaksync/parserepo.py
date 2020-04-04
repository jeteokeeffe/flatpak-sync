from .repolist import repolist
from .repo import repo


class parserepo:

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

            myrepo = repo(cols[name])
            myrepo.setLocation(repo.nameToLocation(cols[name]))
            self.repoList.add(myrepo)

        return True

    def getRepoList(self):
        return self.repoList

