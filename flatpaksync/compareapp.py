from .appreqeust import apprequest

class compareapp:

    def setInstalled(app: apprequest) -> None:
        self.installed = app

    def setConfig(app: apprequest) -> None:
        self.config = app

    def compare() -> str:
        state = 1
        details = {
            1: "{} to be installed".format(self.config.getAppId()),
            2: "{} to be removed".format(self.installed.getAppId()),
            3: "To be upgraded ({} to {})".format(old, new),
            4: "To be downgraded ({} to {})".format(old, new),
            5: "No change, already installed",
            6: "No change, already installed and correct version ({})".format(version),
        }
        return details.get(state)
