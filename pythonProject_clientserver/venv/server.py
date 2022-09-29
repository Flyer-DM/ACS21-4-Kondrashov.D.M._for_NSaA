import socket

sock = socket.socket()  # создание соккета
sock.bind(('', 9090))  # хост общедоступный и порт

flag1, breaker = True, False

while True:
    sock.listen(1)  # включаем режим прослушивания
    if flag1:
        print("Включён режим прослушивания.")
        flag1 = not flag1

    conn, addr = sock.accept()  # получаем новый соккет и адрес клиента
    print("Успешное соединение клиента:", addr[0])

    while True:
        data = conn.recv(1024)  # читаем данные по 1 Кб
        message = data.decode()
        if not message:
            print('Отключение клиента:', addr[0])
            break
        print("Полученное сообщение:", message)
        if message == 'shutdown':
            breaker = not breaker
            break
    if breaker:
        print("Отключение сервера.")
        conn.close()  # закрываем соединение
        break
