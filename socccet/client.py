import socket

from numpy import True_


from server import HOST, PORT

client_socket = socket.socket()

client_socket.connect((HOST, PORT))

def enc(s):
    return s.encode('utf-8')
def dec(s):
    return s.decode('utf-8')
def user_auth(client_socket):
    while True:
        recv_msg = dec(client_socket.recv(1024))
        if recv_msg == '\nUor are in ban list':
            return False
        if recv_msg == 'Auf ok':    
            print(recv_msg)
            return True
        else:
            name = input(recv_msg)
            client_socket.send(enc(name))

try:
    if user_auth(client_socket):    
        while True:
            msg = input('\nType ur msg: \n')
            client_socket.send(enc(msg))
            if msg == 'q':
                break

except KeyboardInterrupt:
    print('n\Client shut down!')
    client_socket.send(enc('q'))
    client_socket.close()
except Exception as e:
    print(e)
    client_socket.close()
client_socket.close()