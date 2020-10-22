import socket
import os
import subprocess
k = socket.socket()
hst = socket.gethostname()
port = 6798
k.bind((hst,port))
print('waiting for connection.........')
k.listen(6)
con,adr = k.accept()
print('connected to : ',adr)
while True:
    dt = input('server : ')
    con.send(dt.encode())
    kl = con.recv(1026).decode()
    if(kl=='exit'):
        break
    else:
        print(subprocess.getoutput(kl))
k.close()





