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
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

    conf = os.environ['HOME'] + '/' + conf
    fp=flatpakcmd()
    if fp.isInstalled() == False:
        sys.exit("Unable to find flatpak! Are you sure flatpak is installed?")

    logging.debug("Flatpak installed: {}".format(fp.isInstalled()))
    logging.debug(fp.getVersion())
    logging.debug("Configuration file: {}".format(conf))

    
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
            logging.info('Successfully wrote configuration')
        else:
            logging.error('Failed to write configuration')

    else:
        logging.echo('Failed to parse apps')


    # Sync (install/remove) applications from your configuration
@cli.command()
@click.option('-v', '--verbose', is_flag=True)
@click.option('-c', '--conf', default=".config/flatpak-sync/app.yaml", help='configuration file')
@click.option('--dryrun', default=0, help='configuration file')
def run(conf, dryrun, verbose):
    """ 
    Run (add/remove) flatpak applications 
    """
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

    conf = os.environ['HOME'] + '/' + conf

    logging.debug("Flatpak installed: {}".format(fp.isInstalled()))
    logging.debug(fp.getVersion())
    logging.debug("Configuration file: {}".format(conf))

    config=readconfig(conf)
    if config.read():
        settings=config.getSettings()
        repolist=config.getRepoList()
        applist=config.getAppList()

            # Install Applications
        for app in applist.getAll():
            action=appaction()
            if action.isInstalled(app):
                logging.info('{} already installed'.format(app.getAppId()))
            else:
                if action.install(app):
                    logging.info('{} installation successful'.format(app.getAppId()))
                else:
                    logging.error('{} installation failed'.format(app.getAppId()))
    else:
        logging.info('failed to read configuration')




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
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

    conf = os.environ['HOME'] + '/' + conf

    logging.debug("Flatpak installed: {}".format(fp.isInstalled()))
    logging.debug(fp.getVersion())
    logging.debug("Configuration file: {}".format(conf))

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
            logging.info('successfully wrote configuration')
        else:
            logging.error('failed to write configuration')

    else:
        logging.error('failed to read configuration')

    




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
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

    conf = os.environ['HOME'] + '/' + conf

    logging.debug("Flatpak installed: {}".format(fp.isInstalled()))
    logging.debug(fp.getVersion())
    logging.debug("Configuration file: {}".format(conf))

    
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
            logging.info('Successfully wrote configuration')
        else:
            logging.error('Failed to write configuration')

    else:
        logging.error('Failed to read configuration')


@cli.command()
@click.option('-v', '--verbose', is_flag=True, help='verbose output')
@click.option('-c', '--conf', default=".config/flatpak-sync/app.yaml", help='configuration file')
def download(conf, verbose):
    """ 
    Download configuration file from remote site

    REPO is the flatpak repository (eg. flathub)
    
    APPID is name of flatpak application (eg. com.gnome.meld)
    """
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

@cli.command()
@click.option('-v', '--verbose', is_flag=True, help='verbose output')
@click.option('-c', '--conf', default=".config/flatpak-sync/app.yaml", help='configuration file')
def upload(conf, verbose):
    """ 
    Upload configuration file to remote site 

    REPO is the flatpak repository (eg. flathub)
    
    APPID is name of flatpak application (eg. com.gnome.meld)
    """
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


@cli.command()
@click.option('-v', '--verbose', is_flag=True, help='verbose output')
@click.option('-c', '--conf', default=".config/flatpak-sync/app.yaml", help='configuration file')
def downloadrun(conf, verbose):
    """ 
    Download and Run configuration file from remote site (Installing Apps and Permissions)

    REPO is the flatpak repository (eg. flathub)
    
    APPID is name of flatpak application (eg. com.gnome.meld)
    """
    

def main():
    cli()
