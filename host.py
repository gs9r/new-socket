import socket
import time

main_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
main_socket.bind(("localhost",10000))

main_socket.setblocking(False)
main_socket.listen(5)
clients = []
while True:
    try:
        new,address = main_socket.accept()
        print(address)
        new.setblocking(False)
        clients.append(new)
    except:
        pass
    for x in clients:
        try:
            data = x.recv(1024).decode()
            print(data)
        except:
            pass
    for y in clients:
        try:
            y.send("hello".encode())
        except:
            clients.remove(y)
            y.close()
            print("socket closed")

    time.sleep(1)

