import socket 
import threading
import sys

HEADER = 64
HOST = ''
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMATO = 'utf-8'
DISCONNECT_mensagem = "!DISCONNECT"

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_input = input("Digite o endereço IP ou pressione ENTER ")
if user_input != '':
    HOST = user_input
user_input = input("Entre com a conexão ou pressione ENTER para porta padrão ")
if user_input != '':
    PORT = int(user_input)
orig = (SERVER, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print("Conectado com ", cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print(cliente, "mensagem enviada : ", str(msg, 'utf-8'))
    print("Conexão com o cliente ", cliente, " encerrada!")
    con.close()