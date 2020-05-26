import sys
import socket
import errno

HEADER_LENGTH = 10

IP = "hboueix.fr"
PORT = 63000


class User:

    def __init__(self, username):
        self.username = username
        self.client_socket = self.get_client_socket()
        self.recv_text = ''

    def get_client_socket(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((IP, PORT))
        client_socket.setblocking(False)

        username = self.username.encode('utf-8')
        username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(username_header + username)
        return client_socket

    def run_connection(self, text):
        #message = input(f"{self.username}> ")
        message = text

        if message:
            message = message.encode("utf-8")
            message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
            self.client_socket.send(message_header + message)

        try:
            while True:
                username_header = self.client_socket.recv(HEADER_LENGTH)
                if not len(username_header):
                    print("Connection fermée par le serveur")
                    sys.exit()

                username_length = int(username_header.decode("utf-8"))
                username = self.client_socket.recv(username_length).decode("utf-8")

                message_header = self.client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode("utf-8"))
                message = self.client_socket.recv(message_length).decode("utf-8")

                self.recv_text = f"{username}> {message}"

        except IOError as e:
            if e.errno != errno.EAGAIN or e.errno != errno.EWOULDBLOCK:
                print('Reading error', str(e))
                sys.exit()

        except Exception as e:
            print('General error', str(e))
            sys.exit()