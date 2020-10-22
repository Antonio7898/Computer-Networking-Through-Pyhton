import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_hst = socket.gethostname()
udp_port = 5973
s.bind((udp_hst,udp_port))
print("Waiting for Client.........")
while True:
    dt,adr = s.recvfrom(2789)
    s.sendto(dt,adr)
    if(dt.decode() == 'quit'):
        break