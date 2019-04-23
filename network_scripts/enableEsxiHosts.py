import paramiko
import time
import re
import os
from getpass import getpass
from threading import Thread

USERNAME = input("USERNAME: ")
PASSWORD = getpass("PASSWORD: ")
#create a list of threads
threads = []

print('run script in the same folder there EsxiHosts.txt is located!')
print('started to read EsxiHosts.txt ')
if os.path.isfile(os.path.join(os.getcwd(), 'EsxiHosts.txt')):
    with open(os.path.join(os.getcwd(), 'EsxiHosts.txt')) as f:
        switches = [line.strip() for line in f]
else:
    print('not found EsxiHosts.txt in current directory')

def run_ssh_cmd(SWITCH,USERNAME,PASSWORD):
    RESULT=[]

    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(SWITCH, username=USERNAME, password=PASSWORD, port=22)

    try:
        channel = client.invoke_shell()
        #channel.send("terminal length 0\n")
        time.sleep(2)
        #channel.send('sh int \n')
        channel.send('sut -set mode=autodeployreboot\n')
        time.sleep(180)
        #channel.send('!---------!\n')
        #channel.send('sh int | include ^..Last.input\n')
        #output1 = output.decode(decoding='utf-8')# command которую нам нужно выполнить
        channel.send('sut -status\n')
        time.sleep(180)
        output = channel.recv(9999).decode(encoding='utf-8')
        #output = channel.recv(5000)
    except Exception as e:
        error_log=str(e)
        print('SOMETHING WENT WRONG (CREDENTIALS OR CONNECTIVITY)')
        print(error_log + '\n')
    #output = channel.recv(99999)
    client.close()
    print('-----------------------',SWITCH,'---------------------------------')
    fileName = SWITCH + '_RESULT.txt'
    print('writing to ./'+fileName+'_RESULT.txt')
    file = open(fileName, 'w')
    file.write(str(output) + "\n")
    # Close the file
    file.close()
    return 0

ind=0
for SWITCH in switches:
    process = Thread(target=run_ssh_cmd, args=[SWITCH,USERNAME,PASSWORD])
    process.start()
    threads.append(process)
    #run_ssh_cmd(SWITCH,USERNAME,PASSWORD)
    ind+=1
    print(ind)
    print('----',switches.index(SWITCH)+1,'/',len(switches),'----',SWITCH,'----')

for process in threads:
    process.join()

print('Everything completed!!!')
#print(output)
