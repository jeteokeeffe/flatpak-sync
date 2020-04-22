import click
import logging

from flatpaksync.commands.add import add as addcmd
from flatpaksync.commands.remove import remove as removecmd
from flatpaksync.commands.run import run as runcmd
from flatpaksync.commands.generate import generate as generatecmd

mylog = logging.getLogger("fps")

@click.group()
def cli():
    pass


@cli.command()
@click.option('-v', '--verbose', is_flag=True, help='verbose output')
@click.option('-c', '--conf', default=".config/flatpak-sync/flatpak.json", help='configuration file')
@click.option('-d', '--dryrun', is_flag=True, help='no action performed')
def generate(conf, dryrun, verbose):
    """ 
    Generate a configuration file from existing,installed flatpak applications 
    """

    cmd = generatecmd()
    cmd.setConfig(conf)
    cmd.setDebug(verbose)
    cmd.setDryRun(dryrun)
    cmd.checkFlatpak()
    cmd.execute()


    # Run (install/remove) applications from your configuration
@click.option('-v', '--verbose', is_flag=True)
@click.option('-c', '--conf', default=".config/flatpak-sync/flatpak.json", help='configuration file')
@click.option('-d', '--dryrun', is_flag=True, help='no action performed')
@cli.command()
def run(conf, dryrun, verbose):
    """ 
    Run (add/remove) flatpak applications 
    """

    cmd = runcmd()
    cmd.setConfig(conf)
    cmd.setDebug(verbose)
    cmd.setDryRun(dryrun)
    cmd.checkFlatpak()
    cmd.execute()





    # Add an Application to be sync'd
@cli.command()
@click.option('-c', '--conf', default=".config/flatpak-sync/flatpak.json", help='configuration file')
@click.option('-v', '--verbose', is_flag=True)
@click.argument('repo')
@click.argument('appid')
def add(repo, appid, conf, verbose):
    """ 
    Add a flatpak application to be managed 

    REPO is the flatpak repository (eg. flathub)
    
    APPID is name of flatpak application (eg. com.gnome.meld)
    """

    cmd = addcmd()
    cmd.setConfig(conf)
    cmd.setDebug(verbose)
    #cmd.setDryRun(dryrun)
    cmd.checkFlatpak()
    cmd.execute(repo, appid)




    # Remove an Application to be sync'd
@cli.command()
@click.option('-c', '--conf', default=".config/flatpak-sync/flatpak.json", help='configuration file')
@click.option('-v', '--verbose', is_flag=True)
@click.argument('repo')
@click.argument('appid')
def remove(repo, appid, conf, verbose):
    """ 
    Remove a flatpak application from being managed

    REPO is the flatpak repository (eg. flathub)
    
    APPID is name of flatpak application (eg. com.gnome.meld)
    """

    cmd = removecmd()
    cmd.setConfig(conf)
    cmd.setDebug(verbose)
    #cmd.setDryRun(dryrun)
    cmd.checkFlatpak()
    cmd.execute(repo, appid)


#@cli.command()
#@click.option('-v', '--verbose', is_flag=True, help='verbose output')
#@click.option('-c', '--conf', default=".config/flatpak-sync/app.yaml", help='configuration file')
#def download(conf, verbose):
#    """ 
#    Download configuration file from remote site
#
#    REPO is the flatpak repository (eg. flathub)
#    
#    APPID is name of flatpak application (eg. com.gnome.meld)
#    """
#    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

#@cli.command()
#@click.option('-v', '--verbose', is_flag=True, help='verbose output')
#@click.option('-c', '--conf', default=".config/flatpak-sync/app.yaml", help='configuration file')
#def upload(conf, verbose):
#    """ 
#    Upload configuration file to remote site 
#
#    REPO is the flatpak repository (eg. flathub)
#    
#    APPID is name of flatpak application (eg. com.gnome.meld)
#    """
#    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


#@cli.command()
#@click.option('-v', '--verbose', is_flag=True, help='verbose output')
#@click.option('-c', '--conf', default=".config/flatpak-sync/app.yaml", help='configuration file')
#def downloadrun(conf, verbose):
#    """ 
#    Download and Run configuration file from remote site (Installing Apps and Permissions)
#
#    REPO is the flatpak repository (eg. flathub)
#    
#    APPID is name of flatpak application (eg. com.gnome.meld)
#    """
    

def main():
    cli()
