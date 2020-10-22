import socket
from getmac import get_mac_address
k = socket.socket()
hst = socket.gethostname()
port = 457
k.bind((hst,port))
print("waiting for connection")
k.listen(4)
con,adr = k.accept()
print("connected to : ",adr)
while True:
    dt = con.recv(1234)
    print("client : ", dt.decode())
    if(dt == 'exit'):
        con.close()
    h7 = adr[0]
    jk = get_mac_address(ip=adr[0], network_request=True)
    con.send(jk.encode())
    break
con.close()