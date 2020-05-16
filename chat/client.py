#!/usr/bin/python3
# -*- coding : utf-8 -*-

import socket
import select
import errno
import sys

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 63000

my_username = input("Username : ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)

while True:
    message = input(f"{my_username} > ")

    if message:
        message = message.encode("utf-8")
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(message_header + message)

    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("Connection fermée par le serveur")
                sys.exit()

            username_length = int(username_header.decode("utf-8"))
            username = client_socket.recv(username_length).decode("utf-8")

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode("utf-8"))
            message = client_socket.recv(message_length).decode("utf-8")

            print(f"{username} > {message}")

    except IOError as e:
        if e.errno != errno.EAGAIN or e.errno != errno.EWOULDBLOCK:
            print('Reading error', str(e))
            sys.exit()
        continue

    except Exception as e:
        print('General error', str(e))
        sys.exit()


'''
import socket

IP_SERVER = "127.0.0.1"
PORT = 63000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP_SERVER, PORT))
client.sendall(bytes("Coucou c'est moi le client", "utf-8"))
while True:
    in_data = client.recv(2048)
    print(f"From server : {in_data.decode()}")
    out_data = input()
    client.sendall(bytes(out_data, 'utf-8'))
    if out_data == 'bye':
        break
client.close()
'''

'''
import socket
import sys
import select

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection_server:
    connection_server.connect(("127.0.0.1", 63000))
    while True:
        sockets_list = [sys.stdin, connection_server]
        read_sockets, write_sockets, error_sockets = select.select(
            sockets_list, [], [])
        for socks in read_sockets:
            if socks == connection_server:
                message = socks.recv(2048)
                print(message)
            else:
                message = sys.stdin.readline()
                connection_server.send(bytes(message, "utf-8"))
                sys.stdout.write("<You>")
                sys.stdout.write(message)
                sys.stdout.flush()
'''

'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection_server:
    connection_server.connect(("164.132.225.71", 63000))
    connection_server.send(bytes("Serveur es-tu là ?", "utf-8"))
    response = connection_server.recv(1024)
    print(response.decode())
'''
