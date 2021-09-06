print('qwikClient')

import socket

#Trivial Strings
tmission = 'transmission!!!'
hiddenId = 'BigRichardJohnson'

#Critical Setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

#Messages Receive
print(socket.gethostname())
msg = s.recv(1024)
print(msg.decode('utf-8'))
msg = s.recv(1024)
print(msg.decode('utf-8'))
msg = s.recv(1024)
print(msg.decode('utf-8'))
print('msg 3 received...?')

#Messages Send
s.send(bytes(tmission, 'utf-8'))

