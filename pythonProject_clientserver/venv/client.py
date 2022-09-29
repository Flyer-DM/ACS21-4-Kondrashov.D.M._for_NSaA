import socket

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))

while True:
    message = input('Введите сообщение для сервера: ')
    print("Отправление сообщения серверу...")
    sock.send(message.encode())
    print("Сообщение успешно доставлено!")
    if message == 'exit':
        break

sock.close()
