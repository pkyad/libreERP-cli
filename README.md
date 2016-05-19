# libreERP-cli

A command line tool to register/de register devices. As of now the only use if this tool is to allow access to the GIT repos on a device.


# Installation

Simply run:

    $ sudo python setup.py install

Apart from this tool you also need GIT. You can install it using

    $ sudo apt-get install git

First time users are recommended to go through the documentation of GIT, however you need to set few things as of now


    $ git config --global user.name "John Doe"
    $ git config --global user.email johndoe@example.com

There is no need of setting some alias for git commands but it can save few seconds each time if you can simple use ` $ git st ` instead of ` $ git status ` and similarly for other common commands. Here is how you setup alias for commands


    $ git config --global alias.co checkout
    $ git config --global alias.br branch
    $ git config --global alias.ci commit
    $ git config --global alias.st status


# Usage

If you have never used SSH on your machine then there is high chances that your machine does not have a ssh key. Generate it using the following command. Press `ENTER` for any prompt you get till you get the message `successfully generated`

    $ ssh-keygen

Register your device to access GIT repos using:

    $ libreerp username@ERPserver:port [optional : action (default : 'login' , options : 'login' , 'logout')]

this will give you the HTTP code as response , if you see success 200 then you are all set.

To see the list of GIT repos you have access to run the following command

    $ ssh git@ERPserver info

If the above command is asking you password then something is not working on your system.

To clone a repo you can use:

    $ git clone git@ERPserver:reponame

To create a personal repo which only you can pull/push to , you can simply use:

    $ git clone git@ERPserver:username/newRepoName

there is no need of creating it from UI

To setup a repo and provide selected users fine grained permissions, you need to login to ERP UI

    1. Project Management > GIT > Repos
    2. Click on `new +` button
    3. Provide the name , Description
    4. Choose if you want to user permission or group permission to this repo.
    5. For group repo you need to you first create a group in Project Management > GIT > Groups
    6. You can search and select the user/group and select the read/write/delete permission values from checkboxes and press Add button
    7. You can continue adding the permissions in the same manner.
    8. Once complete you need to go you Project Management > GIT > Manege and press Sync Gitolite button
