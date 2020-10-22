import socket
j = socket.socket()
hst = socket.gethostname()
port = 457
j.connect((hst,port))
gh = input("task : ")
j.send(gh.encode())
while True:
    dt = j.recv(1234)
    print("mac address : ", dt.decode())
    break
j.close()