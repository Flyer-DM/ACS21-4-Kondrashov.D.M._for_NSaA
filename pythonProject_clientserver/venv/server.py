import socket

sock = socket.socket()  # создание соккета
sock.bind(('', 9090))  # хост общедоступный и порт
sock.listen(1)  # включаем режим прослушивания
print("Включён режим прослушивания.")
conn, addr = sock.accept()  # получаем новый соккет и адрес клиента
print("Успешное соединение клиента:", addr[0])

while True:
    data = conn.recv(1024)  # читаем данные по 1 Кб
    message = data.decode()
    print("Полученное сообщение:", message)
    if message == 'exit':
        print("Отключение от сервера по запросу клиента.")
        break

conn.close()  # закрываем соединение
