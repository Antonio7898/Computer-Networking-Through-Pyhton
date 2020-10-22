import socket
s = socket.socket()
host = socket.gethostname()
port = 6798
s.connect((host,port))
while True :
    print(s.recv(1024).decode())
    jk = input('enter cmd : ')
    s.send(jk.encode())
    if(jk=='exit'):
        break
s.close()
