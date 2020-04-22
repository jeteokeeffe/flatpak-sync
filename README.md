# flatpak-sync
Automate Flatpak Application Installation and Permissions

## Requirements 

* Flatpak (```flatpak --version```)
* Python 3.5 or greater ```python --version```
* PIP installed ```pip --version```

[How to Install Flatpak on your distro](https://flatpak.org/setup/)

## How to Install

After verifying you have Python 3 and pip module manager installed, use the
following command to install.
```
pip install --user flatpak-sync
```

## Usage

### First Step

Install some flatpak applications, change some permissions. When you're happy, run the following command to generate a configuration file.
`flatpak-sync generate -v`

### Now Sync

Okay, you have to setup a new computer. After installing your distro, take your configuration file and just run flatpak-sync

1. Add your flatpak sync configuration file to your desktop ( `$HOME/.config/flatpak-sync/flatpak.json` )
2. Run `flatpak-sync run -v`
3. Done! Flatpak Repositories are setup, applications are installed and permissions are set.

## Commands

Add an Application to your configuration file. This also copies user permissions.
```
flatpak-sync add <repo> <app-id>
flatpak-sync add flathub com.spotify.Client
```

Remove an Application from syncing.
```
flatpak-sync remove <repo> <app-id>
flatpak-sync remove flathub com.spotify.Client
```

Create a configuration file of existing flatpak repositories, applications and permissions.
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

###### I think this feature should be added. How do I get it added?

Create an issue here on github.

###### Is there a list of common flatpak repositories?

Yes, they can be found [here](https://github.com/jeteokeeffe/flatpak-sync/blob/master/data/common-repos.json).

###### Can I add a repository?

Yes, create a Pull Request.

###### Where is the flatpak sync configuration file stored?

`$HOME/.config/flatpak-sync/flatpak.json`

###### Where can I see an example configuration file?

Here is an [example configuration file](https://github.com/jeteokeeffe/flatpak-sync/blob/master/data/flatpak-example.json)

