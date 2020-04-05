# flatpak-sync
Automate Flatpak Application Installation and Permissions

## Requirements 

* Flatpak 1.4 or greater ```gnome-shell --version```
* Python 3.5 or greater ```python --version```
* PIP installed ```pip --version```

[How to Install Flatpak on your distro](https://flatpak.org/setup/)

## How to Install

After verifying you have Python 3 and pip module manager installed, use the
following command to install.
```
pip install --user flatpak-sync
```

## How to Use

Add an Application to your configuration file
```
flatpak-sync add <repo> <app-id>
flatpak-sync add flathub com.spotify.Client
```

Remove an Application
```
flatpak-sync remove <repo> <app-id>
flatpak-sync remove flathub com.spotify.Client
```

Create a list of existing applications and permissions
```
flatpak-sync generate
```

Install and Configure Permissions (Sync)
```
flatpak-sync run
```


Upload & Download
```
flatpak-sync upload
flatpak-sync download
```


Download & Sync 
```
flatpak-sync downloadrun
```

## Questions

Is there a list of common flatpak repositories?
Yes, they can be found [here](https://github.com/jeteokeeffe/flatpak-sync/blob/master/data/common-repos.json)

Where can I see an example configuration file?
Here is an [example configuration file](https://github.com/jeteokeeffe/flatpak-sync/blob/master/data/example-flatpak-configuration.yaml)

