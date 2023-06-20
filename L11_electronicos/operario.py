import socket

HOST = 'localhost'  # Dirección IP del servidor
PORT = 5000  # Puerto del servidor

def recibir_datos():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = s.recv(1024).decode()
            print(data)

if __name__ == '__main__':
    recibir_datos()
