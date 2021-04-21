import socket
import threading
from Constants import *

my_socket = socket.socket()

def connect():
    name = input('enter your name: ')
    my_socket.connect((SERVER_IP, SERVER_PORT))
    _server_name = my_socket.recv(1024).decode()
    print(_server_name, 'is the host!')
    print('You joined!')
    my_socket.send(bytes(name, ENCODING_METHOD))
    thread = threading.Thread(target=receive_messages)
    thread.start()


def receive_messages():
    while True:
        try:
            s = my_socket.recv(1024).decode()
            if s=='GAME STARTED!':
                print(s)
                play_game(my_socket)
                break
            else:
                print(s + ' has joined the game!')
        except:
            print('an error occured')
            my_socket.close()
            break


def play_game(_my_socket):
    _score = 0
    _my_socket.send(bytes('play game inititation',ENCODING_METHOD))
    for i in range(NUMBER_OF_ROUNDS):
        print('round', i + 1)
        word = _my_socket.recv(1024).decode()
        _my_socket.send(bytes(DATA_RECEIVED, ENCODING_METHOD))
        blank_query = _my_socket.recv(1024).decode()
        print('\t\t', blank_query)
        _my_response = input('Enter your response: ')
        _score += calculate_difference(word, _my_response)
        print('waiting for other players...')
        _my_socket.send(bytes(FLAG_RESPONSE_SUBMITTED, ENCODING_METHOD))
        _my_socket.recv(1024)
        print('Correct word was:', word)
    end_game(_my_socket, _score)


def end_game(my_socket,score):
    my_socket.send(bytes(str(score),ENCODING_METHOD))
    s = my_socket.recv(1024).decode()
    print(s)
    input()
    close_connection(my_socket)


def close_connection(_my_socket):
    _my_socket.close()


try:
    connect()
except ConnectionError as e:
    print('Game already started!', e)
