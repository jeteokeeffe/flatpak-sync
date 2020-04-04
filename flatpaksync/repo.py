
class repo:

    '''
    flatpak repository
    '''
    def __init__(self, name = '', location = ''):
        self.name = name
        self.location = location

    def setName(self, name: str) -> None:
        self.name = name

    def setLocation(self, location: str) -> None:
        self.location = location

    def getName(self) -> str:
        return self.name

    def getLocation(self) -> str:
        return self.location


    def nameToLocation(name) -> str:
        switcher = {
            "flathub": "https://flathub.org/repo/flathub.flatpakrepo",
            "flathub-beta": "https://flathub.org/beta-repo/flathub-beta.flatpakrepo",
            "fedora": "oci+https://registry.fedoraproject.org",
            "gnome-nightly": "https://nightly.gnome.org/gnome-nightly.flatpakrepo",
            "kdeapps": "https://distribute.kde.org/kdeapps.flatpakrepo"
        }
        return switcher.get(name, "invalid-repo")
