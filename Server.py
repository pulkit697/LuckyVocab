import socket
from Constants import *

score = 0
serverSocket = socket.socket()
serverSocket.bind((SERVER_IP, SERVER_PORT))
name = input('enter name: ')
print('You are the host!')
serverSocket.listen(1)
while True:
    clientSocket, clientAddress = serverSocket.accept()
    break
clientSocket.send(bytes(name, ENCODING_METHOD))
clientName = clientSocket.recv(1024).decode()
print(clientName, 'joined.')

for i in range(NUMBER_OF_ROUNDS):
    print('round', i + 1)
    word = choose_random_word()
    blank_query = return_blank_string(word, 2)
    clientSocket.send(bytes(word, ENCODING_METHOD))
    data_received = clientSocket.recv(1024).decode()
    clientSocket.send(bytes(blank_query, ENCODING_METHOD))
    print('\t\t', blank_query)
    myResponse = input('Enter your response: ')
    score += calculate_difference(word, myResponse)
    print('waiting for other players...')
    clientSocket.recv(1024)
    clientSocket.send(bytes(FLAG_ALL_SUBMISSIONS_RECEIVED, ENCODING_METHOD))
    print('Correct word was:', word)

print('Your score is:', score)
clientSocket.send(bytes(str(score), ENCODING_METHOD))
oppositeScore = int(clientSocket.recv(1024).decode())
if oppositeScore > score:
    print(clientName, ' won!')
elif oppositeScore == score:
    print('Game draw!!!')
else:
    print('You won!!!')
serverSocket.close()
