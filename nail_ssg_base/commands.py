import sys
import click
# from .site_builder import SiteBuilder

from .builder import Builder as SiteBuilder


@click.group(chain=True)
def cli1():
    pass


@cli1.command('prepare')
@click.argument('directory', default='pages', type=str)
def prepare(directory=None):
    """prepare"""
    print('prepare', directory)


@click.group(chain=True)
def cli2():
    pass


@cli2.command('build')
@click.argument('configfile', default='.config.yml', type=str)
def build(configfile=None):
    """build"""
    site_builder = SiteBuilder(configfile)
    site_builder.build()

cli = click.CommandCollection(sources=[cli1, cli2])


def run(argv=None):
    argv = argv or sys.argv[:]
    cli()
