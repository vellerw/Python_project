import os
import threading
import socket

list_nickname = []
list_client = []


def authoruzation(client):
    while True:                                                              #cпрашивает, пока не будет результата
        client.send("Ваш ник".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')                         #спрашивает клиента о нике
        print(nickname)
        if nickname not in list_nickname:                                    #проверяет ник в списке никнеймов
            client.send("Успешно".encode('utf-8'))
            break
        else:
            client.send("Этот ник уже использован".encode('utf-8'))          #такой никнейм уже есть
            continue
    return nickname


def choosen(client):                                                         #выбор клиента
    print(list_nickname)
    string_choose = ''
    for user, nick in zip(range(len(list_client)), list_nickname):           #создаем удобный список пользователей
        string_choose += '{0}.{1}'.format(user + 1, nick) + " "
    while True:
        client.send(f"Выберите номер:\n {string_choose}".encode('utf-8'))
        try:
            usernum = int(client.recv(1024).decode('utf-8'))                 #пользователь должен ввести цифру
        except Exception:
            continue
        if 0 < usernum <= len(list_client):                                  #проверка на правильное число
            choose_user = list_nickname[usernum - 1]
        if choose_user:                                                      #если выбранный пользователь существует, то возвращаем клиента по индексу ника
            client.send("Успешно".encode('utf-8'))
            return list_client[list_nickname.index(choose_user)]
        else:
            client.send("В чате никого".encode('utf-8'))                     #если никого не будет в чате


def chat(client, client_to_connect):
    while True:
        try:                                                                 #обработчик ошибок
            message = client.recv(1024).decode('utf-8')
            nick = list_nickname[list_client.index(client)]                  #для удобства введения никнейма
            client_to_connect.send(f"{nick} : {message}".encode('utf-8'))    #форма получаемого сообщения (Nickname : Message)
        except Exception:
            print("break from ", list_nickname[list_client.index(client)])   #если кто-то вышел, удаляем его из списка, закрываем соединение
            list_nickname.pop(list_client.index(client))
            list_client.remove(client)
            client.close()
            client_to_connect.close()
            break


def new_client(client):
    nickname = authoruzation(client)                                          #ник от клиента, подключились
    if nickname == None:                                                      #если никнейм не выбран, то закрываем клиента
        client.close()
    list_nickname.append(nickname)                                            #заносим в список никнеймов и клиентов(потом поиск будет происходить по индексу)
    list_client.append(client)
    client.send("Вы готовы?".encode('utf-8'))                                 #после ввдеения ника, пользователь должен немного подождать, чтобы появился выбор, иначе он будет один на сервере
    if client.recv(1024).decode('utf-8') != "":                               #если пользователь не вышел
        client_to_connect = choosen(client)                                   #функция для выбора собеседника
        chat(client, client_to_connect)                                       #функция для чата 1 на 1
    else:
        print("break from ", list_nickname[list_client.index(client)])        #пишем кто вышел, и удаляем его из списков. Закрываем этого клиента
        list_nickname.pop(list_client.index(client))
        list_client.remove(client)
        client.close()


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          #создаем сокет
    server_socket.bind(("127.0.0.1", 12345))                                   # Ip и порт, на которых сервер будет работать и слушать, связываем с портом
    server_socket.listen()
    print('Сервер начал работать')
    try:
        while True:
            client_socket, address = server_socket.accept()                    #принимаем все подключения к серверу
            print('Соедиение с ' + str(address))                               #наши местные журналы
            thread = threading.Thread(target=new_client, args=(client_socket,))
            # Обработать пользователя, чтобы общаться с другими пользователями, затем можно вернуться, чтобы прослушать новых подключенных пользователей
            thread.daemon = True                                               #пользователи будут находиться в чате до тех пор, пока не захотят выйти
            thread.start()                                                     #запуск процесса
    except KeyboardInterrupt:
        print('Пока')
        server_socket.close()
        os._exit(0)
