import socket

SERVER_IP = "0.0.0.0"
SERVER_PORT = 10004

# for i in range(10000):
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((SERVER_IP, SERVER_PORT))
#     s.sendall(b"Hello from the client")
#
#     s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_IP, SERVER_PORT))
s.sendall(b"Naman")
response = ""
data = s.recv(1024)
print(data)
s.close()