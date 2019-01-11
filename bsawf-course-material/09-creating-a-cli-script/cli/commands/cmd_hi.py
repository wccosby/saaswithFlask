import subprocess
import click

@click.command()
@click.argument('name', default="please give me a name!")
@click.argument('path', default='snakeeyes')
def cli(name, path):
    """
    Say Hi using an arugment

    :param name: Who to say hi to
    :param path: root path
    :Return: Informal greeting
    """
    cmd = 'echo Hi {}'.format(name)
    return subprocess.call(cmd, shell=True)