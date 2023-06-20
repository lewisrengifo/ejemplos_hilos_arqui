import socket
import random
import time

SOCK_BUFFER = 1024


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("127.0.0.1", 7000)  
    
    print(f"Conectando a servidor : {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)
    while True:
        try:
            data_recibida = sock.recv(SOCK_BUFFER)
            inicio_envio = data_recibida.decode()
            if inicio_envio == "S":
                print("Enviando presion al servidor...")
                valor_presion = str(random.randint(5, 20))
                data = sock.sendall(valor_presion.encode())
                time.sleep(0.5)
        except Exception as e:
            print(e)
            print("Cerrando conexion")
            sock.close()
            break
        