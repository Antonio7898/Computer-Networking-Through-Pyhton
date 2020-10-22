import socket
from datetime import datetime
j = socket.socket()
hst = socket.gethostname()
port = 659
j.connect((hst,port))
while True:
    gh = datetime.now()
    print(datetime.now())
    j.send(str(gh).encode())
    dt = j.recv(1234)
    print("server : ",str(dt).encode())
j.close()