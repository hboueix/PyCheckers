import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection_server:
    connection_server.connect(("164.132.225.71", 63000))
    connection_server.send(bytes("Serveur es-tu là ?", "utf-8"))
    response = connection_server.recv(1024)
    print(response.decode())
