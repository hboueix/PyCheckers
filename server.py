#!/usr/bin/python3
# -*- coding : utf-8 -*-

import socket
import select
import sys

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 63000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]

clients = {}


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8'))

        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
        return False


while True:
    try:
        read_sockets, _, exception_sockets = select.select(
            sockets_list, [], sockets_list
        )

        for notified_socket in read_sockets:
            if notified_socket == server_socket:
                client_socket, client_address = server_socket.accept()

                user = receive_message(client_socket)
                if user is False:
                    continue

                sockets_list.append(client_socket)

                clients[client_socket] = user

                print(
                    f"Nouvelle connection depuis {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}"
                )

            else:
                message = receive_message(notified_socket)

                if message is False:
                    print(
                        f"Connection terminée avec {clients[notified_socket]['data'].decode('utf-8')}"
                    )
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    continue

                user = clients[notified_socket]
                print(
                    f"Message reçu de {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}"
                )

                for client_socket in clients:
                    if client_socket != notified_socket:
                        client_socket.send(
                            user['header'] + user['data'] + message['header'] + message['data'])

        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            del clients[notified_socket]

    except KeyboardInterrupt:
        print('\nExtinction du serveur...')
        sys.exit()


'''
import socket
import threading


class ClientThread(threading.Thread):

    def __init__(self, clientAddress, clientSocket):
        threading.Thread.__init__(self)
        self.cSocket = clientSocket
        print(f'Nouvelle connexion : {clientAddress}')

    def run(self):
        print(f'Connexion depuis : {clientAddress}')
        self.cSocket.send(
            bytes("Le serveur te salue ...!\nÉcris 'bye' pour te déco", 'utf-8')
        )
        msg = ''
        while True:
            data = self.cSocket.recv(2048)
            msg = data.decode()
            if msg == 'bye':
                break
            print(f"From client {msg}")
            self.cSocket.send(bytes(msg, 'utf-8'))
        print(f"Client {clientAddress} disconnected...")


# IP et port du serveur
IP_SERVER = "127.0.0.1"
PORT = 63000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((IP_SERVER, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(50)
    clientSocket, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientSocket)
    newthread.run()
'''


'''
import socket
import sys
from _thread import *

def client_thread(connection_client, address_client):
    connection_client.send(b"Bienvenue dans la chatroom !")

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

'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listen_socket:
    listen_socket.bind(("", 63000))
    listen_socket.listen()
    connection_client, address_client = listen_socket.accept()
    print(address_client)
    message = connection_client.recv(1024)
    connection_client.send(bytes(message.decode() + "\nPrésent !", "utf-8"))
'''
