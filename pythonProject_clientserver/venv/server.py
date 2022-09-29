import socket

sock = socket.socket()  # создание соккета
sock.bind(('', 9090))  # хост общедоступный и порт
sock.listen(1)  # включаем режим прослушивания
conn, addr = sock.accept()  # получаем новый соккет и адрес клиента
print(addr)

msg = ''

while True:
    data = conn.recv(1024)  # читаем данные по 1024 Кб
    if not data:  # как только клент перестаёт отправлять данные
        break
    msg += data.decode()
    conn.send(data)  # возвращаем сообщение клиента

print(msg)

conn.close()  # закрываем соединение
