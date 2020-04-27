import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listen_socket:
    listen_socket.bind(("", 63000))
    listen_socket.listen()
    connection_client, address_client = listen_socket.accept()
    print(address_client)
    message = connection_client.recv(1024)
    connection_client.send(bytes(message.decode() + "\nPrésent !", "utf-8"))
