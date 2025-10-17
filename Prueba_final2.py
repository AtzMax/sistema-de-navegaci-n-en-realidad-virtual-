import socket
from pynput.keyboard import Controller

keyboard = Controller()

UDP_IP = "0.0.0.0"   # Escucha en todas las interfaces
UDP_PORT = 4210

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("Esperando datos UDP...")

while True:
    data, addr = sock.recvfrom(1024)
    estado = data.decode().strip()

    print("Recibido:", estado)  # Esto sí lo verás en consola (debug)

    if estado == "0":   # Quieto
        keyboard.release('a')
        keyboard.release('d')

    elif estado == "1": # Derecha
        keyboard.press('d')
        keyboard.release('a')

    elif estado == "2": # Izquierda
        keyboard.press('a')
        keyboard.release('d')

    elif estado == "3": # Ambos → detener
        keyboard.release('a')
        keyboard.release('d')
