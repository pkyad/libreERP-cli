# libreERP-cli

A command line tool to register/de register devices. As of now the only use if this tool is to allow access to the GIT repos on a device.


# Installation

You will need to change the IP address of the server in the libreerp/cli.py file and build the solution and then install.

If you don't use `pipsi`, you're missing out.
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Simply run:

    $ pipsi install .


# Usage

To use it:

    $ libreerp [username] [password] [optional : action (default : 'login')]
