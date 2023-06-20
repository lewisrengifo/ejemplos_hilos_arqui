import socket
import threading
import time

def recibir_presion(client_socket):
    while True:
        # Recibir datos del sensor de presión
        mensaje = client_socket.recv(1024).decode()
        
        # Obtener el tiempo de recepción del dato
        tiempo_actual = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        
        # Calcular la profundidad en metros
        presion = float(mensaje.split(': ')[1].split(' ')[0])  # Extraer el valor de presión
        profundidad = presion / (1023.6 * 9.81)
        
        # Enviar la profundidad al operario
        mensaje_profundidad = f'Profundidad: {profundidad} metros (Tiempo: {tiempo_actual})'
        operario_socket.send(mensaje_profundidad.encode())

def recibir_oxigeno(client_socket):
    while True:
        # Recibir datos del sensor de oxígeno disuelto
        mensaje = client_socket.recv(1024).decode()
        
        # Obtener el tiempo de recepción del dato
        tiempo_actual = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        
        # Enviar los datos de oxígeno disuelto al operario
        mensaje_oxigeno = f'Oxigeno disuelto: {mensaje} (Tiempo: {tiempo_actual})'
        operario_socket.send(mensaje_oxigeno.encode())

# Configurar el servidor
host = 'localhost'  # Cambia esto por la dirección IP o nombre de host del servidor
port = 5000  # Puerto del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(3)  # Esperar conexiones del sensor de presión, sensor de oxígeno y operario

print('Esperando conexiones...')
presion_socket, presion_address = server_socket.accept()
oxigeno_socket, oxigeno_address = server_socket.accept()
operario_socket, operario_address = server_socket.accept()

print('Sensor de presion conectado')
print('Sensor de oxigeno conectado')
print('Operario conectado')

print('Empezando transmision')

# Crear hilos para recibir y enviar datos
presion_thread = threading.Thread(target=recibir_presion, args=(presion_socket,))
oxigeno_thread = threading.Thread(target=recibir_oxigeno, args=(oxigeno_socket,))
presion_thread.start()
oxigeno_thread.start()

# Mantener el programa en ejecución hasta que se interrumpa
try:
    while True:
        pass
except KeyboardInterrupt:
    print('Programa terminado')
    server_socket.close()
    operario_socket.close()
