# flatpak-sync
Automate Flatpak Application Installation and Permissions

## Requirements 

* Flatpak 1.4 or greater ```flatpak --version```
* Python 3.5 or greater ```python --version```
* PIP installed ```pip --version```

[How to Install Flatpak on your distro](https://flatpak.org/setup/)

## How to Install

After verifying you have Python 3 and pip module manager installed, use the
following command to install.
```
pip install --user flatpak-sync
```

## Basic Usage

After you've installed flatpak on your distro
1. Install your flatpak applications, set some permissions
2. Generate a flatpak sync configuration file
`flatpak-sync generate`


Okay, you have to setup a new computer. After installing your distro, take your configuration file and just run flatpak-sync

1. Add your flatpak sync configuration file to your desktop
2. Run `flatpak-sync run`
3. Done!

## Commands

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

Create a list of existing flatpak applications and permissions
```
flatpak-sync generate
```

Install flatpak applications and configure permissions (Sync)
```
flatpak-sync run
```


## Recommendations

Chezmoi is a command line tool to easily manage your dotfiles with git. 
https://github.com/twpayne/chezmoi
https://fedoramagazine.org/take-back-your-dotfiles-with-chezmoi/

Flatseal is a GUI application that makes adding permissions to your flakpak applications easy.
https://flathub.org/apps/details/com.github.tchx84.Flatseal
https://www.omgubuntu.co.uk/2020/02/flatseal-manage-flatpak-permissions

## Bug Reports

Creae an issue and post these things
* Distro (`hostnamectl`)
* Flatpak version (`flatpak --version`)
* Flatpak-sync configuration file (`~/.config/flatpak-sync/flatpak.json`) file

## Questions

###### Is there a list of common flatpak repositories?

Yes, they can be found [here](https://github.com/jeteokeeffe/flatpak-sync/blob/master/data/common-repos.json).

###### Can I add a repository?

Yes, create a Pull Request.

###### Where is the flatpak sync configuration file stored?

`$HOME/.config/flatpak-sync/flatpak.json`

###### Where can I see an example configuration file?

Here is an [example configuration file](https://github.com/jeteokeeffe/flatpak-sync/blob/master/data/flatpak-example.json)

