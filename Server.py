# import socket
from tkinter import *
from Constants import *

clients = []
names = []
server_socket = socket.socket()
server_socket.bind((SERVER_IP, SERVER_PORT))

def connect():
    name = input('enter name: ')
    print('You are the host!')
    server_socket.listen()
    while True:
        client_socket, client_address = server_socket.accept()
        client_socket.send(bytes(name, ENCODING_METHOD))
        client_name = client_socket.recv(1024).decode()
        print(client_name+' has joined...')
        broadcast_message(client_name)
        names.append(client_name)
        clients.append(client_socket)
        if len(clients) == 3:
            broadcast_message('GAME STARTED!')
            break
    play_game()


def broadcast_message(message):
    print(message)
    for client in clients:
        client.send(bytes(message, ENCODING_METHOD))
        print('sent!')


def receive_from_all():
    for i in range(len(clients)):
        clients[i].recv(1024)
        print('received from',names[i])


def play_game():
    receive_from_all()
    for i in range(NUMBER_OF_ROUNDS):
        print('round', i + 1)
        word = choose_random_word()
        blank_query = return_blank_string(word, 2)
        broadcast_message(word)
        receive_from_all()
        broadcast_message(blank_query)
        print('\t\t', word, '\t\t', blank_query)
        receive_from_all()
        broadcast_message('sending new word...')
    end_game()


def end_game():
    scores = []
    for client in clients:
        scores.append(int(client.recv(1024).decode()))
    maxim = 0
    index = 0
    result = ''
    for i in range(len(scores)):
        result+=names[i]+' : '+str(scores[i])+'\n'
        if scores[i] > maxim:
            maxim = scores[i]
            index = i
    result+='Winner is: \n' + names[index] +'\n 🤩🤩🤩🤩🤩🤩🤩'
    broadcast_message(result)
    close_connection()


def close_connection():
    server_socket.close()

connect()

