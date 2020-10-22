import socket
j = socket.socket()
hst = socket.gethostname()
port = 457
j.connect((hst,port))
gh = input("Enter Data")
j.send(gh.encode())
while True:

    dt = j.recv(1234)
    print("server : ",dt.decode())
    gh = input("Client : ")
    j.send(gh.encode())

j.close()