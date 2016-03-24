import click
import os
import requests

@click.command()
@click.option('--logout', '-c', is_flag=True, help='logout.')
@click.option('--login', '-c', is_flag=True, help='login.')
@click.argument('username', default='', required=False)
@click.argument('password', default='', required=False)
def main(username , password , logout , login):
    """My Tool does one thing, and one thing well."""
    mode = 'login'
    if login:
        mode = 'login'
    if logout:
        mode = 'logout'
    sshKey = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read()
    r = requests.post("http://192.168.56.1:8000/api/git/registerDevice/",
                json={
                  'username': username,
                  'password': password,
                  'sshKey': sshKey,
                  'mode':mode
                }
            )
    if r.status_code ==200:
        outText = 'Success'
    else:
        outText = 'Error'
    click.echo('{0}-: {1}'.format(r.status_code , outText))
