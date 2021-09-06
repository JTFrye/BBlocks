print('qwikServe .0')

import socket

#Critical Setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)


whatUwant = 'This is what u want!\n'
anotherMessageCuz = 'Just to see if it works\n'

#Listener
while True:
    clientsocket, address = s.accept()
    print('connecteded')
    clientsocket.send(bytes("Hello, msg from server!\n", 'utf-8'))
    print(address, ' has connected')
    clientsocket.send(bytes(whatUwant, 'utf-8'))
    clientsocket.send(bytes(anotherMessageCuz, 'utf-8'))
    #receive section
    newMsg = clientsocket.recv(1024)
    print(newMsg.decode('utf-8'))
    
    
