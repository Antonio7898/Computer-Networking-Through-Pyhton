import socket
j = socket.socket()
hst = socket.gethostname()
port = 659
j.connect((hst,port))
while True:
    j.send(input("client : ").encode())
    dt = j.recv(1234)
    print("server : ",dt.decode())
j.close()