import socket
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
    print("client : ",dt.decode())
    jk = input("Server : ")
    con.send(jk.encode())
co.close()