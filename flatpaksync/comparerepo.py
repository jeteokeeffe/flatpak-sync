


class comparerepo:

    def setInstalled(self, repo):
        self.installed = repo
        return true


    def setConfig(self, repo):
        self.config = repo
        return true


    def compare():
        if (self.installed)
            state = 3
        else
            state = 1

        details = {
            1: "{} repository to be installed",
            2: "{} repository to be removed",
            3: "No change, {} already installed"
        }
        return details.get(state)
