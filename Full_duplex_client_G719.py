import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port =  678
s.connect((host,port))
def recv():
    while True:
        dt = s.recv(256)
        print('Server : ',dt.decode())
        if(dt.decode()=='quit'):
            break
def snd():
    while True:
        dt = input('Client : ')
        s.send(dt.encode())
        if (dt == 'quit'):
            break
t1 = threading.Thread(target=snd)
t2 = threading.Thread(target=recv)
t1.start()
t2.start()
