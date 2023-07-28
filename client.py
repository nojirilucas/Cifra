import socket
import sys

HEADER = 64
PORT = 5050
SERVER = "192.168.0.116"
ADDR = (SERVER, PORT)
FORMATO = 'utf-8'
DISCONNECT_mensagem = "DESCONECTADO"

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_input = input("Digite o endereço IP ou pressione ENTER ")
if user_input != '':
    SERVER = user_input
user_input = input("Entre com a conexão ou pressione ENTER para porta padrão ")
if user_input != '':
    PORT = int(user_input)
servidor = (SERVER, PORT)
tcp.connect(servidor)
print("Para sair use CTRL + C\n")
msg = input("Digite a mensagem: ")
while msg != '\x18':
    tcp.send(str.encode(msg))
    msg = input("Mensagem à enviar: ")
tcp.close()   