import socket
<<<<<<< HEAD

ClientSocket = socket.socket()
host = '192.168.56.102'
port = 8889

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))
    exit()
ClientSocket.close()
=======
import sys
import json

s = socket.socket()

port = 8080

s.connect(('192.168.56.102', port))

data = s.recv(1024)
data = data.decode("utf-8")

s.send(b'Thank you from client!');

dataJ = json.loads(data)

print (type(dataJ))
print(dataJ)

s.close()
>>>>>>> d12959f165c2c7fefbc74f9795083fe83ddb1d77
