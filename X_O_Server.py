from socket import *
from _thread import *

class TicTacToeServer:
    def __init__(self, host, port):
        self.s = socket(AF_INET, SOCK_STREAM)
        self.host = host
        self.port = port
        self.s.bind((self.host, self.port))
        self.s.listen(2)  
        self.clients = []

    def handle_client(self, c):
        while True:
            try:
                button_number = int(c.recv(1024).decode('utf-8'))
                for client in self.clients:
                    if client != c:
                        client.send(str(button_number).encode('utf-8'))
            except ValueError:
                break

    def start_server(self):
        while True:
            c, ad = self.s.accept()
            self.clients.append(c)
            start_new_thread(self.handle_client, (c,))

if __name__ == '__main__':
    server = TicTacToeServer("127.0.0.1", 7772)
    server.start_server()
