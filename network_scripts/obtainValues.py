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

for SWITCH in switches:

    RESULT=[]

    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())



    client.connect(SWITCH, username=USERNAME, password=PASSWORD, port=22)

    try:
        channel = client.invoke_shell()
        channel.send("terminal length 0\n")
        time.sleep(2)
        #channel.send('sh int \n')
        channel.send('sh int | include (down|up).+(down|up)\n')
        time.sleep(5)
        #channel.send('!---------!\n')
        channel.send('sh int | include ^..Last.input\n')
        #output1 = output.decode(decoding='utf-8')# command которую нам нужно выполнить
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

    #ll=output.split('\n')
    ll = [item.strip() for item in output.split('\n')]
    #ll=map(str.strip, ll)
    interfaces=[]
    interfacesStatuses=[]

    #print(output1)
    for _ in ll:
        if ('#' in _) or ( not _) or ('*' in _):
            pass #print('line removed')
        else:
            if ('Last input' in _):
                interfacesStatuses.append(_)
            else:
                interfaces.append(_)

    for interface, status in zip(interfaces,interfacesStatuses):
        if len(interface) != 1:
            words = re.findall(r'\w+', interface.replace("/", ""))
            if words[2]=='down' or words[2]=='administratively' :
                words = re.findall(r'\w+', status)
                duration=words[2]
                if duration=='never':
                    RESULT.append(str(SWITCH+'---'+interface+'---'+status))
                    #print(interface,'------',status)
                elif 'y' in duration:
                    RESULT.append(str(SWITCH+'---'+interface+'---'+status))
                elif 'w' in duration: # in case last input greater than 6 weeks
                    ind=duration.index('w')
                    if int(duration[0:ind]) >= 6 :
                        RESULT.append(str(SWITCH+'---'+interface+'---'+status))
                        #print(interface,'------',status)        
                    #period[0:3]
                    #print(interf,'------',status)

    

    fileName = SWITCH + '_RESULT.txt'
    print('writing to ./'+fileName+'_RESULT.txt')
    file = open(fileName, 'w')
    for _ in RESULT:
        file.write(str(_) + "\n")
    # Close the file
    file.close()

print('COMPLETED')
time.sleep(10)
