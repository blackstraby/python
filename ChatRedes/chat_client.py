from socket import *
import pyaudio
import wave
import _thread as thread

host = '192.168.0.109'
port = 50000

user = input("Digite seu nick: ")
# Abrir conexao AF_INET = familia de protocolos
# TCP = SOCK_STREAM / UDP = sockDATAGRAM
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((host, port))

print("Chat is running!")


def receive_data():
    while True:
        try:
            # data = recebe pacote de mensagem com maximo de 1024 bits
            data = sockobj.recv(1024)
            print('', '\n')
            # decodifica os bits para e string
            print(data.decode())
            print(user + ':'),
        except:
            print("Erro ao receber mensagem")


def send_data():
    while True:
        try:
            msg = input(user + ": ",)
            msg = user + ':' + msg
            # Encoda a mensagem 'Usuario: mensagem' para bits
            sockobj.send(msg.encode())
        except:
            print("Erro ao enviar mensagem")


# Thread para poder enviar e receber mensagens de diferentes clientes conectados
thread.start_new_thread(send_data, ())
thread.start_new_thread(receive_data, ())

# Enquanto true executa ('pass' não faz nada)
while True:
    pass
