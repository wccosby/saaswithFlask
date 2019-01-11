import subprocess
import click

@click.command()
@click.option('--name', prompt='Your name', help='The person to greet')
@click.argument('path', default='snakeeyes')
def cli(name, path):
    """
    Say hello

    :param path: default path
    :param name: person's name
    :return: Greeting
    """
    # click.echo("Hello {}".format(name))

    cmd = 'echo Hello {}'.format(name)
    return subprocess.call(cmd, shell=True)