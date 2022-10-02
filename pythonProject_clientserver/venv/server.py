import socket
import datetime
import random
import hashlib

f = open('log.txt', 'w')

sock = socket.socket()  # создание сокета
average_port = 9090
while True:
    try:
        sock.bind(('', average_port))
        print("Используется порт: " + str(average_port))
        break
    except OSError as error:
        print("{} (порт {} занят)".format(error, average_port))
        average_port = random.randint(1024, 65535)

flag1, breaker, attempts = True, False, 3

while True:
    sock.listen(1)  # включаем режим прослушивания
    if flag1:
        print("Включён режим прослушивания.")
        f.write("Включён режим прослушивания." + ' | ' + str(datetime.datetime.now()) + '\n')
        flag1 = not flag1

    conn, addr = sock.accept()  # получаем новый сокет и адрес клиента
    with open('clinets.txt', 'a+') as clients_list:
        clients_list.seek(0, 0)
        #  поиск имеющегося клиента
        for line in clients_list:
            if addr[0] in line:
                f.write("Подключение известного клиента: " + addr[0] + ' | ' + str(datetime.datetime.now()) + '\n')
                conn.send('known'.encode())
                conn.send(("Здравствуйте, " + line[line.index('|') + 1:line.rindex('|')]).encode())
                while True:
                    conn.send("Введите свой пароль: ".encode())
                    f.write("Запрос пароля клиента: " + addr[0] + ' | ' + str(datetime.datetime.now()) + '\n')
                    password = conn.recv(1024).decode()
                    if line[line.rindex('|') + 1:] == hashlib.md5(password.encode()).hexdigest():
                        conn.send("true".encode())
                        conn.send("Вы подтвердили свой пароль!".encode())
                        f.write("Клиент подтвердил свой пароль" + ' | ' + str(datetime.datetime.now()) + '\n')
                        break
                    else:
                        attempts -= 1
                    if attempts == 0:
                        conn.send('false'.encode())
                        conn.send("Количество попыток исчерпано!".encode())
                        break
                break
        else:
            #  запись нового клиента с его паролем и именем
            conn.send('new'.encode())  # флаг, означающий первое подключение клиента
            conn.send("Вы незарегистрированный пользователь! Введите ваше имя: ".encode())  # 1 сообщение клиенту
            name = conn.recv(1024).decode()  # 1 сообщение от клиента
            conn.send("Введите пароль: ".encode())  # 2 сообщение клиенту
            password = conn.recv(1024).decode()  # 2 сообщение от клиента
            password = hashlib.md5(password.encode()).hexdigest()  # хешерование пароля
            clients_list.write('\n' + addr[0] + '|' + name + '|' + password)
            f.write("Запись нового клиента: " + addr[0] + ' | ' + str(datetime.datetime.now()) + '\n')

    if attempts != 0:
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
