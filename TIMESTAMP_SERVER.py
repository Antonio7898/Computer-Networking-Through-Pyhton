from datetime import datetime
print(datetime.now())
import socket
from datetime import datetime
k = socket.socket()
hst = socket.gethostname()
port = 659
k.bind((hst,port))
print("waiting for connection")
k.listen(5)
co,adr = k.accept()
print("connected to : ",adr)
while True:

    dt = co.recv(1234)
    print("client : ",str(dt).encode())
    gh = datetime.now()
    co.send(str(gh).encode())

co.close()