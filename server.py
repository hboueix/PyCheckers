import socket
import sys
from _thread import *

def client_thread(connection_client, address_client):
    connection_client.send("Bienvenue dans la chatroom !")

    while True:
        try:
            message = connection_client.recv(2048)
            if message:
                print(f'<{address_client[0]}> {message}')
                message_to_send = "<" + address_client[0] + ">" + message
                broadcast(message_to_send, connection_client)
            else:
                remove(connection_client)
        except:
            continue

def broadcast(message, connection_client):
    for client in list_of_clients:
        if client != connection:
            try:
                client.send(message)
            except:
                client.close()
                remove(client)

def remove(connection_client):
    if connection_client in list_of_clients:
        list_of_clients.remove(connection_client)

list_of_clients = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listen_socket:
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(("164.132.225.71", 63000))
    listen_socket.listen(100)
    while True:
        connection_client, address_client = listen_socket.accept()
        list_of_clients.append(connection_client)
        print(f'{address_client[0]} connected')
        start_new_thread(client_thread, (connection_client, address_client))

'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listen_socket:
    listen_socket.bind(("", 63000))
    listen_socket.listen()
    connection_client, address_client = listen_socket.accept()
    print(address_client)
    message = connection_client.recv(1024)
    connection_client.send(bytes(message.decode() + "\nPrésent !", "utf-8"))
'''
