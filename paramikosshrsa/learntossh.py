#!/usr/bin/env python3

##import paramiko so that we can talk SSH
import paramiko
import os

##shortcut issuing commands to remote
def commandissue(command_to_issue):
  ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
  return ssh_stdout.read()

sshsession = paramiko.SSHClient()

## mykey is our privatekey
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

##creds to connect
sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]

for x in our_commands:
    print(commandissue(x))

