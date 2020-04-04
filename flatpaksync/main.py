import click
import logging
import os

from .readconfig import readconfig
from .writeconfig import writeconfig
from .appaction import appaction
from .app import app
from .repoaction import repoaction
from .parseapp import parseapp
from .parserepo import parserepo
from .settings import settings
from .flatpakcmd import flatpakcmd



@click.group()
def cli():
    pass


@cli.command()
@click.option('-v', '--verbose', is_flag=True, help='verbose output')
@click.option('-c', '--conf', default=".config/flatpak-sync/app.yaml", help='configuration file')
def generate(conf, verbose):
    """ 
    Generate a configuration file from existing/installed flatpak applications 
    """

    conf = os.environ['HOME'] + '/' + conf
    fp=flatpak()
    if fp.isInstalled() == False:
        sys.exit("Unable to find flatpak! Are you sure flatpak is installed?")

    if verbose:
        print("Flatpak installed: {}".format(fp.isInstalled()))
        print(fp.getVersion())
        print()
        print("Configuration file: {}".format(conf))

    
    raction=repoaction() 
    output = raction.list()
    rparse=parserepo()
    rparse.parse(output)

    action=appaction() 
    output=action.list()
    parse=parseapp()

    if parse.parse(output):

        fpsettings = settings()
        applist = parse.getAppList()
        repolist = rparse.getRepoList()

            # Write configuration
        wconfig = writeconfig(conf)
        wconfig.setSettings(fpsettings)
        wconfig.setRepoList(repolist)
        wconfig.setAppList(applist)

        if wconfig.write():
            click.echo('Successfully wrote configuration')
        else:
            click.echo('Failed to write configuration')

    else:
        click.echo('Failed to parse apps')


    # Sync (install/remove) applications from your configuration
@cli.command()
@click.option('-v', '--verbose', is_flag=True)
@click.option('-c', '--conf', default=".config/flatpak-sync/app.yaml", help='configuration file')
@click.option('--dryrun', default=0, help='configuration file')
def sync(conf, dryrun, verbose):
    """ 
    Sync (add/remove) flatpak applications 
    """

    conf = os.environ['HOME'] + '/' + conf
    if verbose:
        fp=flatpak()
        print("Flatpak installed: {}".format(fp.isInstalled()))
        print(fp.getVersion())
        print()
        print("Configuration file: {}".format(conf))

    config=readconfig(conf)
    if config.read():
        settings=config.getSettings()
        repolist=config.getRepoList()
        applist=config.getAppList()

            # Install Applications
        for app in applist.getAll():
            action=appaction()
            if action.isInstalled(app):
                click.echo('{} already installed'.format(app.getAppId()))
            else:
                if action.install(app):
                    click.echo('{} installation successful'.format(app.getAppId()))
                else:
                    click.echo('{} installation failed'.format(app.getAppId()))
    else:
        click.echo('failed to read configuration')




    # Add an Application to be sync'd
@cli.command()
@click.option('-c', '--conf', default=".config/flatpak-sync/app.yaml", help='configuration file')
@click.option('-v', '--verbose', is_flag=True)
@click.argument('repo')
@click.argument('appid')
def add(repo, appid, conf, verbose):
    """ 
    Add a flatpak application to be managed 

    REPO is the flatpak repository (eg. flathub)
    
    APPID is name of flatpak application (eg. com.gnome.meld)
    """

    conf = os.environ['HOME'] + '/' + conf
    if verbose:
        fp=flatpak()
        print("Flatpak installed: {}".format(fp.isInstalled()))
        print(fp.getVersion())
        print()
        print("Configuration file: {}".format(conf))

    config=readconfig(conf)
    if config.read():
        settings=config.getSettings()
        repolist=config.getRepoList()
        applist=config.getAppList()

        addApp=app(appid, repo)
        applist.add(addApp)

            # Write configuration
        wconfig = writeconfig(conf)
        wconfig.setSettings(settings)
        wconfig.setRepoList(repolist)
        wconfig.setAppList(applist)

        if wconfig.write():
            click.echo('successfully wrote configuration')
        else:
            click.echo('failed to write configuration')

    else:
        click.echo('failed to read configuration')

    




    # Remove an Application to be sync'd
@cli.command()
@click.option('-c', '--conf', default=".config/flatpak-sync/app.yaml", help='configuration file')
@click.option('-v', '--verbose', is_flag=True)
@click.argument('repo')
@click.argument('appid')
def remove(repo, appid, conf, verbose):
    """ 
    Remove a flatpak application from being managed

    REPO is the flatpak repository (eg. flathub)
    
    APPID is name of flatpak application (eg. com.gnome.meld)
    """

    conf = os.environ['HOME'] + '/' + conf
    if verbose:
        fp=flatpak()
        print("Flatpak installed: {}".format(fp.isInstalled()))
        print(fp.getVersion())
        print()
        print("Configuration file: {}".format(conf))

    
    config=readconfig(conf)
    if config.read():

        settings=config.getSettings()
        repolist=config.getRepoList()
        applist=config.getAppList()

            # Remove an App from the list
        removeApp=app(appid, repo)
        applist.remove(removeApp)

            # Write configuration
        wconfig = writeconfig(conf)
        wconfig.setSettings(settings)
        wconfig.setRepoList(repolist)
        wconfig.setAppList(applist)

        if wconfig.write():
            click.echo('Successfully wrote configuration')
        else:
            click.echo('Failed to write configuration')

    else:
        click.echo('Failed to read configuration')


def main():
    cli()
