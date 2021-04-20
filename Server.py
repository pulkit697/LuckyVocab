import socket
from tkinter import *
from Constants import *


def connect():
    server_socket = socket.socket()
    server_socket.bind((SERVER_IP, SERVER_PORT))
    name = input('enter name: ')
    print('You are the host!')
    server_socket.listen(1)
    while True:
        client_socket, client_address = server_socket.accept()
        break
    client_socket.send(bytes(name, ENCODING_METHOD))
    client_name = client_socket.recv(1024).decode()
    print(client_name, 'joined.')
    return server_socket, client_socket, client_name


def play_game(client_socket):
    score = 0
    for i in range(NUMBER_OF_ROUNDS):
        print('round', i + 1)
        word = choose_random_word()
        blank_query = return_blank_string(word, 2)
        client_socket.send(bytes(word, ENCODING_METHOD))
        data_received = client_socket.recv(1024).decode()
        client_socket.send(bytes(blank_query, ENCODING_METHOD))
        print('\t\t', blank_query)
        my_response = input('Enter your response: ')
        score += calculate_difference(word, my_response)
        print('waiting for other players...')
        client_socket.recv(1024)
        client_socket.send(bytes(FLAG_ALL_SUBMISSIONS_RECEIVED, ENCODING_METHOD))
        print('Correct word was:', word)
    return score


def end_game(client_socket, client_name, _score):
    print('Your score is:', _score)
    client_socket.send(bytes(str(_score), ENCODING_METHOD))
    opposite_score = int(client_socket.recv(1024).decode())
    if opposite_score > _score:
        print(client_name, ' won!')
    elif opposite_score == _score:
        print('Game draw!!!')
    else:
        print('You won!!!')


def close_connection(server_socket):
    server_socket.close()


serverSocket, clientSocket, clientName = connect()
score = play_game(clientSocket)
end_game(clientSocket, clientName, score)
close_connection(serverSocket)
