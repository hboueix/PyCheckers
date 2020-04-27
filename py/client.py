import socket
import sys
import select

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection_server:
    connection_server.connect(("164.132.225.71", 63000))
    while True:
        socket_list = [sys.stdin, connection_server]
        read_sockets, write_sockets, error_sockets = select.select(sockets_list,[],[])
        for socks in read_sockets:
            if socks == connection_server:
                message = socks.recv(2048)
                print(message)
            else:
                message = sys.stdin.readline()
                server.send(bytes(message, "utf-8"))
                sys.stdout.write("<You>") 
                sys.stdout.write(message) 
                sys.stdout.flush() 

'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection_server:
    connection_server.connect(("164.132.225.71", 63000))
    connection_server.send(bytes("Serveur es-tu là ?", "utf-8"))
    response = connection_server.recv(1024)
    print(response.decode())
'''
