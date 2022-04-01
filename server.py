import socket
import threading
import time

HOST = "0.0.0.0" # localhost
PORT = 10004

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4 or ipv6 + type of transport (tcp or UDP)
conn_place = (HOST, PORT)
s.bind(conn_place)
s.listen()

# def handleConnection(conn, addr):
#     time.sleep(5)
#     print("Connected to " + str(addr[0]) + " " + str(addr[1]))

def handleConnection(conn, addr):
    name = ""
    data = conn.recv(1024)
    conn.sendall(data)


while True:
    conn, addr = s.accept()
    thread = threading.Thread(target=handleConnection,
                              args=(conn, addr))
    thread.start()
    if (threading.active_count() > 500):
        print("WAIT")
    print("Number of threads at this time = " + str(threading.active_count()))

s.close()