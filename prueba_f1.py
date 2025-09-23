import socket
from pynput.keyboard import Controller, Key

keyboard = Controller()

UDP_IP = "0.0.0.0"  # Escucha en todas las interfaces
UDP_PORT = 4210

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("Esperando datos UDP...")

while True:
    data, addr = sock.recvfrom(1024)
    estado = data.decode().strip()

    if estado == "0":   # 00 = quieto
        keyboard.release(Key.left)
        keyboard.release(Key.right)

    elif estado == "1": # 01 = derecha
        keyboard.press(Key.right)
        keyboard.release(Key.left)

    elif estado == "2": # 10 = izquierda
        keyboard.press(Key.left)
        keyboard.release(Key.right)

    elif estado == "3": # 11 = ambos tocados → detener
        keyboard.release(Key.left)
        keyboard.release(Key.right)

#ESTE ES SOLO UN EJEMPLO