![image](https://user-images.githubusercontent.com/113033685/196170018-7d28de0b-b73b-445c-b91d-1249069052dc.png)

1. Создание соединения между-клиент сервером:

![image](https://user-images.githubusercontent.com/113033685/196170299-bce76a8d-2843-4a8e-88b0-8de1cbb8385d.png)
![image](https://user-images.githubusercontent.com/113033685/196170298-25de0849-cdac-4235-ae2d-b652cbcfc6b5.png)

2. Добавление функционала разрыва соединения со стороны клиента по сообщению "exit":

![image](https://user-images.githubusercontent.com/113033685/196170381-d29560e8-ab17-4d27-89e5-1ca68c08ff4a.png)
![image](https://user-images.githubusercontent.com/113033685/196170387-ff54f4e7-4c72-4bec-84b8-ebd02687829d.png)

3. Добавление постоянного прослушивания порта сервером до получения команды "shutdown":

![image](https://user-images.githubusercontent.com/113033685/196170421-70611784-6cbb-482b-8d86-c4166f0f2294.png)
![image](https://user-images.githubusercontent.com/113033685/196170433-574ab4f7-4cb0-4ce3-9f55-170d520aa45b.png)

4. Добавление ввода адреса и порта для клиента с ограничением количества попыток:

![image](https://user-images.githubusercontent.com/113033685/196170465-1be62d79-eb88-4556-a5a4-97782c2b864c.png)

5. Добавление записи служебных сообщений в отдельный файл:

![image](https://user-images.githubusercontent.com/113033685/196170495-b2a91e8d-f966-4e37-a916-e966fc66e0d1.png)

6. Добавление автоматической генерации номера порта для сервера:
![image](https://user-images.githubusercontent.com/113033685/196170524-9a7cc510-0527-40d1-9f4e-1479293b26e3.png)

7. Запрос сервера имени подключённого пользователя и запись новых пользователей и их IP серверов в отдельный файл

![image](https://user-images.githubusercontent.com/113033685/196170685-8c572caa-da02-49a3-822d-2fa3760cf2f1.png)
![image](https://user-images.githubusercontent.com/113033685/196170704-386ac562-97d0-4985-accd-33d0755fa387.png)
![image](https://user-images.githubusercontent.com/113033685/196170714-ab5e94f3-9cde-44ce-a5b6-f1872736c5b7.png)

8. Сервер аутентификации. Теперь он запрашивает пароль у пользователя при входе или регистрирует пользователя, если он заходит впервые. Пароли хранятся в отдельном файле, зашифрованные методом md5.

Подключение к серверу и регистрация:

![image](https://user-images.githubusercontent.com/113033685/196170894-9205c536-44b1-4ce7-893b-4d919bdafad6.png)

Повторное подключение к работающему серверу:

![image](https://user-images.githubusercontent.com/113033685/196171018-87f30dea-7d83-429e-a107-1a22574c7553.png)

Записи сервера:

![image](https://user-images.githubusercontent.com/113033685/196171075-7e00c5ac-e203-4428-aada-f7144ce69bcf.png)

Лог файл истории работы сервера:

![image](https://user-images.githubusercontent.com/113033685/196171119-d8620d46-9993-4065-95af-f8e59e9659a2.png)

Как хранится запись о пользователе в отдельном файле:

![image](https://user-images.githubusercontent.com/113033685/196171165-b5ec37a3-06be-4488-a541-7eb97e950d0c.png)

9. Написаны дополнительные функции для отправки и получения сообщений:

![image](https://user-images.githubusercontent.com/113033685/196171274-f907f0c2-29ed-45ef-aa28-fc5fca932df5.png)

![image](https://user-images.githubusercontent.com/113033685/196171294-9a3aed43-f740-4ed7-9f90-5ac1c97338b9.png)



Многопользовательский чат:

![image](https://user-images.githubusercontent.com/113033685/196171385-019e5db2-ff35-4e22-a252-ab107537d8ed.png)
