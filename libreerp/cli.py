import click
import os
import requests
from getpass import getpass
from ui import getLibreUser , getConfigs

@click.command()
@click.argument('connection', default='', required=True)
@click.option('--action', default='login', required=False , help="action can be either login or logout , default is login")
@click.option('--mode', default='c', required=False , help = "input mode can be ither u means user interface , or a command line c")
@click.option('--proxy', default=None, required=False , help = "provide proxy connection string in the format username:password@server:port")
def main(connection,action , mode , proxy):

    if mode == 'u':
        # in this mode the user need to provide the url for the ERP not the username@ERP format
        confs = getConfigs()
        if confs is None:
            confs = {'domain' : connection}
        else:
            if connection != '':
                confs['domain'] = connection
        if proxy is not None:
            confs['proxy'] = {
            'http': proxy,
            'https' : proxy,
            }
        print confs

        confFilePath = os.path.expanduser('~/.libreerp/config.txt')
        f = open(confFilePath , 'w')
        lines = []
        for key in confs:
            if key == 'proxy':
                value = confs[key]['http']
            else:
                value = confs[key]
            if value is None:
                continue
            lines.append('%s=%s\n' % (key , value))
        f.writelines(lines)
        f.close()
        u = getLibreUser()
        print u

    else:
        # command line mode

        parts = connection.split('@')
        if len(parts)<2:
            print 'Please provide username@server value or type libreerp --help to know more'
            exit()
        username = parts[0]
        server = parts[1]
        password = getpass('Enter your password:')
        sshKey = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read()
        r = requests.post("http://" + server + "/api/ERP/registerDevice/",
                    json={
                      'username': username,
                      'password': password,
                      'sshKey': sshKey,
                      'mode':action
                    }
                )
        if r.status_code ==200:
            outText = 'Success'
        else:
            outText = 'Error'
        click.echo('{0}-: {1} , {2}'.format(r.status_code , outText , server))
