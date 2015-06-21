import socket
   

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('introctf.me', 22222))
print s.recv(4096)

while True:
    s.sendall(str(eval(s.recv(4096).strip())) + '\n')
    print s.recv(4096)

s.close()
