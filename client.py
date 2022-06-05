import os
import threading
import socket


def recv(client_socket):
    while True:                                                #бесконечный цикл получения сообщения
        message = client_socket.recv(1024).decode('utf-8')     #получаем сообщение
        if len(message) == 0:                                  #проверка на закрытие сервера или отключения собеседника
            break
        if ":" in message :
            nick, arg = message.split(":")
            if len(arg) == 0:
                break
        else:
            print("\n Входящее сообщение: \n ", message, "\n")
    client_socket.close()                                      #если вышли из цикла, закрываем клиента и закрываем программу
    os._exit(0)


def send(client_socket):
    try:                                                       #обработчик ошибок
        while True:
            message = input()
            if message == "q":                                 #если пользователь выходит
                client_socket.close()
                os._exit(0)
                break
            else:
                client_socket.send(message.encode('utf-8'))
    except Exception:
        print("Сервер закрылся")
        client_socket.close()
        os._exit(0)


client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 12345))
thread_sent = threading.Thread(target=send, args=(client_socket,))#задаем процесс отправки сообщения
thread = threading.Thread(target=recv, args=(client_socket,))   #процесс получения сообщения
thread.start()                                                  #запускаем процесс получения сообщения первым, чтобы отправка сообщений не перекрывала этот процесс
thread_sent.start()                                             #процесс отправки сообщения
