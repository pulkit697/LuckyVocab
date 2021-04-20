import socket

from Constants import *

score = 0
mySocket = socket.socket()
name = input('enter name: ')
try:
    mySocket.connect((SERVER_IP, SERVER_PORT))
    print(mySocket.recv(1024).decode(), 'is the host!')
    print('You joined!')
    mySocket.send(bytes(name, ENCODING_METHOD))
    for i in range(NUMBER_OF_ROUNDS):
        print('round', i + 1)
        word = mySocket.recv(1024).decode()
        mySocket.send(bytes(DATA_RECEIVED, ENCODING_METHOD))
        blank_query = mySocket.recv(1024).decode()
        print('\t\t', blank_query)
        myResponse = input('Enter your response: ')
        score += calculate_difference(word, myResponse)
        print('waiting for other players...')
        mySocket.send(bytes(FLAG_RESPONSE_SUBMITTED, ENCODING_METHOD))
        mySocket.recv(1024)
        print('Correct word was:', word)
    print('Your score is:', score)
    mySocket.send(bytes(str(score), ENCODING_METHOD))
    oppositeScore = int(mySocket.recv(1024).decode())
    if oppositeScore > score:
        print('Opposition won!')
    elif oppositeScore == score:
        print('Game draw!!!')
    else:
        print('You won!!!')
except ConnectionResetError:
    print('Game already started!')
mySocket.close()
