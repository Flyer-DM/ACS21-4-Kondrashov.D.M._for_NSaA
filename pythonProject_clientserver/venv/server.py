import socket
import datetime
import random

f = open('log.txt', 'w')

sock = socket.socket()  # создание соккета
average_port = 9090
while True:
    try:
        sock.bind(('', average_port))
        print("Используется порт: " + str(average_port))
        break
    except OSError as error:
        print("{} (порт {} занят)".format(error, average_port))
        average_port = random.randint(1024, 65535)

flag1, breaker = True, False

while True:
    sock.listen(1)  # включаем режим прослушивания
    if flag1:
        print("Включён режим прослушивания.")
        f.write("Включён режим прослушивания." + ' | ' + str(datetime.datetime.now()) + '\n')
        flag1 = not flag1

    conn, addr = sock.accept()  # получаем новый соккет и адрес клиента
    with open('clinets.txt', 'a+') as clients_list:
        clients_list.seek(0, 0)
        for line in clients_list:
            if addr[0] in line:
                conn.send(("Здравствуйте, " + line.replace(addr[0], '')).encode())
                f.write("Подключение известного клиента: " + addr[0] + ' | ' + str(datetime.datetime.now()) + '\n')
                break
        else:
            conn.send("Вы незарегистрированный пользователь! Введите ваше имя: ".encode())
            name = conn.recv(1024).decode()
            clients_list.write('\n' + addr[0] + name)
            f.write("Запись нового клиента: " + addr[0] + ' | ' + str(datetime.datetime.now()) + '\n')
    print("Успешное соединение клиента: " + addr[0])
    f.write("Успешное соединение клиента: " + addr[0] + ' | ' + str(datetime.datetime.now()) + '\n')

    while True:
        data = conn.recv(1024)  # читаем данные по 1 Кб
        message = data.decode()  # декодирование битов в текст
        if not message:
            print('Отключение клиента: ', addr[0])
            f.write("Отключение клиента: " + addr[0] + ' | ' + str(datetime.datetime.now()) + '\n')
            break
        print("Полученное сообщение :", message)
        f.write("Полученное сообщение: " + message + ' | ' + str(datetime.datetime.now()) + '\n')
        if message == 'shutdown':
            breaker = not breaker
            break
    if breaker:
        print("Отключение сервера.")
        f.write("Отключение сервера." + ' | ' + str(datetime.datetime.now()) + '\n')
        conn.close()  # закрываем соединение
        break

f.close()
