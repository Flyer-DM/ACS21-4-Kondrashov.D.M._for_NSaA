import socket
import re

sock = socket.socket()
attempts, flag1, flag2 = 3, True, False  # флаги: количество попыток, номер порта

try:
    while True:
        ip_add_server = input('Введите IP адрес сервера (имя хоста): ')
        port_server = input('Введите номер порта сервера: ')
        try:
            port_server = int(port_server)
            flag2 = True
        except ValueError:
            flag2 = False
        if re.match('^localhost|(\d{3}\.\d{3}\.\d{3}\.\d{3})$', ip_add_server) is None or not flag2:
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
        flag3 = sock.recv(1024).decode()
        if flag3 == 'new':
        #  впервые подлючаюсь к серверу
            print(sock.recv(1024).decode())  # имя пользователя
            sock.send(input().encode())
            print(sock.recv(1024).decode())  # пароль пользователя
            sock.send(input().encode())
        elif flag3 == 'known':
        #  повторное подключение (я известный пользователь)
            print(sock.recv(1024).decode() + '\n' + sock.recv(1024).decode())  # приветствие по имени и запрос пароля)
            while True:
                sock.send(input().encode())  # отправка пароля
                flag3 = sock.recv(1024).decode()  # получение флага, верен пароль или нет
                if flag3 == 'true':
                    print(sock.recv(1024).decode())  # сервер подтверждает верность пароля
                    break
                elif flag3 == 'false':
                    print(sock.recv(1024).decode())  # если количество попыток исчерпано
                    break
                else:
                    print(flag3)
        if flag3 in ('new', 'true'):
            while True:
                message = input('Введите сообщение для сервера: ')
                print("Отправление сообщения серверу...")
                sock.send(message.encode())
                print("Сообщение успешно доставлено!")
                if message in ('exit', 'shutdown'):
                    print('Закрытие соединения.')
                    break

    sock.close()
except (OSError, ConnectionRefusedError, TimeoutError):
    print("Ошибка ввода адреса сервера, либо сервер не работает!")
