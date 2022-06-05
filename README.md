# Проектное задание
 ## Задачи:
 * Cписок пользователей
 * Пользователи могут общаться друг с другом
 * Сервер отправляет сообщение со списком пользователей для общения на выбор
 * Оформление кода


# Структура проектного задания:
1. Суть задания, как работает, какие технологии используются
2. Теоретическая часть
3. Практическая часть: код с описанием
4. Скриншоты работ
5. Вывод 

## Используемые модули:
* os
* threading
* socket

# Теоретическая часть
-  Os - модуль os позволяет работать с файловой системой, с окружением, управлять процессами.

- Socket - это программный интерфейс для обеспечения информационного обмена между процессами. 

- Threading - модуль для реализации многопоточности в программах на Python.  Threading использует потоки, а не процессы. А еще модуль реализует поток как функцию.

### Существуют 
* Клиентский сокет - подключается к серверу.
* Серверный сокет -  прослушивает определенный порт. 

### Сокеты работают на транспортном уровне и бывают 2 типов:
* Потоковые (на основе TCP) - сокеты с установленным соединением передают поток байтов, который может быть двунаправленным, может и получать и отправлять данные.

* Дейтаграммные (на основе UDP) - сокеты, не требующие установления явного соединения между ними.
### В python для работы с сокетами используется встроенная библиотека socket
```
class socket.socket
sock = socket.socket()
```
```socket.bind(address)``` - Привязывает сокет к адресу address (инициализирует IP-адрес и порт). Сокет не должен быть привязан до этого.

```socket.listen([backlog])``` - Переводит сервер в режим приема соединений.

### Разделение потоков и процессов
* Процесс — является исполняемой программой. В контексте процесса работает один или несколько потоков.
* Поток — определенный способ выполнения процесса. Основные модули программы, среди которых операционная система распределяет процессорное время. 

### Преимущества потоков
* Поток можно завершить намного быстрее, чем процесс.
* Экономия ресурсов внешней и внутренней памяти.
* При использовании потоков повышается эффективность обмена информацией между двумя программами.

# Практическая часть
# *Сервер*
```
#импортируемые модули
import os
import threading
import socket

#словари
list_nickname = []
list_client = []

#авторизация пользователя
def authoruzation(client)

#функция для выбора пользователя
def choosen(client: socket) -> str

#функция чата, общение пользователей
def chat(client:socket, client_to_connect:socket):

#отправка сообщений пользователю    ???????????
client_to_connect.send(message: str, client: socket)

#авторизация и начало потока 
def new_client()

#вызов потока в функции def new_client()
thread = threading.Thread(target=new_client, args=(client_socket,))
thread.start()  

#основной модуль вызова программы сервера
if __name__ == '__main__'
```
# *Клиент*
```
#функция принятия сообщений
def recv()

#функция принятия сообщений
def send()

#модуль подключения
client_socket = socket.socket()
client_socket.connect((str(ip), int(port))
thread_sent = threading.Thread(target=send, args=(client_socket,))
thread = threading.Thread(target=recv, args=(client_socket,))
thread.start()
thread_sent.start()
```
# Фотодоказательства
<a href="https://ibb.co/FsWTGmc"><img src="https://i.ibb.co/JxdJXm8/photoeditorsdk-export.png" alt="photoeditorsdk-export" border="0"></a>

начало работы сервера

<a href="https://ibb.co/gdrnZ1n"><img src="https://i.ibb.co/MfgXkTX/photoeditorsdk-export-1.png" alt="photoeditorsdk-export-1" border="0"></a>

подключение пользователей

<a href="https://ibb.co/BBrF8c9"><img src="https://i.ibb.co/L1JH4Y3/photoeditorsdk-export-2.png" alt="photoeditorsdk-export-2" border="0"></a>

выбор пользователей

<a href="https://ibb.co/FBv4NXP"><img src="https://i.ibb.co/2j23mSb/photoeditorsdk-export-3.png" alt="photoeditorsdk-export-3" border="0"></a>

отправка и прием соообщения

<a href="https://ibb.co/HzdGCxB"><img src="https://i.ibb.co/Xs8FD3j/photoeditorsdk-export-4.png" alt="photoeditorsdk-export-4" border="0"></a>

нет повторного добавления пользователя, т.к. он есть в базе

# Вывод
Проект выполнен, README написано, пойду готовиться к сессии. У меня все.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/Bcw8RQy/shkolnik-116169065-orig-1.jpg" alt="shkolnik-116169065-orig-1" border="0"></a>
