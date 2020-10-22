import socket
j = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_hst = socket.gethostname()
udp_port = 5973
while True:
    gh = input("client : ")
    j.sendto(gh.encode(),(udp_hst,udp_port))
    dt,adr= j.recvfrom(1024)
    print("server : ",dt.decode())
    if(dt.decode()=='quit'):
        break
j.close()