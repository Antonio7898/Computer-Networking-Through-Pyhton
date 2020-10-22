import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port =  678
s.bind((host,port))
print("waiting for connection...........")
s.listen(6)
con,adr = s.accept()
print('connected to :',adr)
def snd():
    while True:
        dt = input('Server : ')
        con.send(dt.encode())
        if (dt == 'quit'):
            break

def recv():
    while True:
        dt = con.recv(256)
        print('CLient : ',dt.decode())
        if(dt.decode()=='quit'):
           break
t1 = threading.Thread(target=snd)
t2 = threading.Thread(target=recv)
t1.start()
t2.start()

