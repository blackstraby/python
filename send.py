# coding - utf-8
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "x"*1024

ip = "192.168.0.107"
port = 666
duration = 3

timeout = time.time() + duration

sent = 0

while True:
    if time.time() > timeout:
        break
    else:
        pass
    try:
        sock.sendto(msg.encode(), (ip, port))
    except socket.error as x:
            print(x)

    sent = sent + 1
    print("Enviado " + str(sent) + " pacotes para " + ip)



