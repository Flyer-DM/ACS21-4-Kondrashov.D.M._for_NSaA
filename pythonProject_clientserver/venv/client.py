import socket
import re

sock = socket.socket()
attempts, flag1, flag2 = 3, True, False
while True:
    ip_add_server = input('Введите IP адрес сервера (имя хоста): ')
    port_server = input('Введите номер порта сервера: ')
    try:
        port_server = int(port_server)
        flag2 = True
    except ValueError:
        flag2 = False
    if re.match('^localhost|[\d{3}.\d{3}.\d{3}.\d{3}$]', ip_add_server) is None or not flag2:
        print("Ошибка ввода данных!")
        attempts -= 1
    else:
        break
    if attempts == 0:
        print("Количество попыток подключения исчерпано!")
        flag1 = False
        break
if flag1:
    print("Успешное подключение к серверу!")
    sock.connect((ip_add_server, port_server))  # имя хоста и номер порта
    print("Сообщение от сервера:", sock.recv(1024).decode())
    while True:
        message = input('Введите сообщение для сервера: ')
        print("Отправление сообщения серверу...")
        sock.send(message.encode())
        print("Сообщение успешно доставлено!")
        if message in ('exit', 'shutdown'):
            print('Закрытие соединения.')
            break

sock.close()
