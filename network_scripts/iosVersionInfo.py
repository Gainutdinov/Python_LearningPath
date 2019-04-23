import paramiko
import time
import re
import os
from getpass import getpass

USERNAME = input("USERNAME: ")
PASSWORD = getpass("PASSWORD: ")


print('run script in the same folder there switches.txt is located!')
print('started to read switches.txt ')
if os.path.isfile(os.path.join(os.getcwd(), 'switches.txt')):
    with open(os.path.join(os.getcwd(), 'switches.txt')) as f:
        switches = [line.strip() for line in f]
else:
    print('not found switches.txt in current directory')

RESULT=[]
    
for SWITCH in switches:

    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(SWITCH, username=USERNAME, password=PASSWORD, port=22)

    try:
        channel = client.invoke_shell()
        channel.send("terminal length 0\n")
        time.sleep(2)
        #channel.send('sh int \n')
        channel.send('sh version\n')
        time.sleep(5)
        output = channel.recv(9999).decode(encoding='utf-8')
        #output = channel.recv(5000)
    except Exception as e:
        error_log=str(e)
        print('SOMETHING WENT WRONG (CREDENTIALS OR CONNECTIVITY)')
        print(error_log + '\n')
    #output = channel.recv(99999)
    print('----',switches.index(SWITCH)+1,'/',len(switches),'----',SWITCH,'----')
    client.close()
    ll = [item.strip() for item in output.split('\n')]

    RESULT.append("-------------------------"+SWITCH+"-------------------------")
    for _ in ll:
        if ('Base ethernet MAC Address' in _) or \
           ('Model number' in _) or \
           ('System serial number ' in _):
            RESULT.append(_)
        elif ('Switch Ports Model' in _):
            for item in ll[ll.index(_):ll.index(_)+3]:
                RESULT.append(item)
    

fileName = 'RESULT.txt'
print('writing to ./RESULT.txt')
file = open(fileName, 'w')
for _ in RESULT:
    file.write(str(_)+"\n")
file.close()
print('COMPLETED')
time.sleep(10)
