import socket
import select

# Classe ChatServer
# 'self' em python é como se fosse 'this' em Java


class ChatServer:
    def __init__(self):

        self.LISTA_CONEXOES = []
        self.chatSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.chatSocket.bind(("0.0.0.0", 50000))
        self.chatSocket.listen(5)

        self.LISTA_CONEXOES.append(self.chatSocket)

        print("Server Online!")

    def broadcast(self, sock, data):
        # Para o socket atual na lista de conexoes
        for socket_atual in self.LISTA_CONEXOES:
            if socket_atual != self.chatSocket and socket_atual != sock:
                try:
                    socket_atual.send(data)
                except:
                    pass

    def run(self):
        while True:
            rlist, wlist, xlist = select.select(self.LISTA_CONEXOES, [], [])

            for socket_atual in rlist:
                if socket_atual is self.chatSocket:
                    (novo_socket, address) = self.chatSocket.accept()
                    self.LISTA_CONEXOES.append(novo_socket)
                    print("%s conectou-se no server" % str(address))
                else:
                    try:
                        data = socket_atual.recv(1024)
                        # Envia para todos na rede
                        self.broadcast(socket_atual, data)
                    except socket.error:
                        print("%s saiu do server" % str(address))
                        # Fecha conexao e remove da lista
                        socket_atual.close()
                        self.LISTA_CONEXOES.remove(socket_atual)


# Metodo main
if __name__ == "__main__":
    try:
        ChatServer().run()
    except KeyboardInterrupt:
        print("\nAte mais.\n")
        exit()
