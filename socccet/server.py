
from codecs import BufferedIncrementalEncoder
import socket
from pprint import pprint
import threading
import sqlite3

connection = sqlite3.connect(database=str('baneedlist')) # запрос бан листа имен
cursor = connection.cursor()
cursor.execute('select  * from ban')
ban_list = cursor.fetchall()
print(ban_list)
baneed_names = []
for i in ban_list:
    baneed_names.append(i[0])

ban_list = baneed_names
print(baneed_names)

ban_list_addresses = dict()
cursor.execute('select  * from banaddress')
ban_list_addres= cursor.fetchall()
print(ban_list_addres)

for i in ban_list_addres:
    ban_list_addresses[i[0]] = i[1],i[2]

print(ban_list_addresses)


HOST = '127.0.0.1'
PORT = 12350


def enc(s):
    return s.encode('utf-8')
def dec(s):
    return s.decode('utf-8')
def usernamesss():
    global users
    a = users.keys()
    res = []
    for i in a:
        res.append(i)
    return res

def new_client(client_socket, username):
    global users
    while True:
        recv_msg = client_socket.recv(1024)
        print('\nIncoming msg: \n')
        decoded = dec(recv_msg)
        if decoded == 'show table':
            pprint(users)
            
        else:
            print('User {0[0]}:{0[1]}:'. format(username), decoded)
            pprint(users)
            if decoded == 'q':
                del users[username]
                print('user {0} disconnected'.format(username))
                pprint(users)
                break

def server_auth(user):
    k = 0
    while True:
        if k == 0:
            user.send(enc('Type your name:'))
        else:
            user.send(enc('Type another name:'))
        username = dec(user.recv(1024))
        if username in ban_list:
            user.send(enc('\nN\n'))
        else:
            if username not in users.keys():
                if address[0] in ban_list_addresses.keys():
                    pass
                    # if address[1] > ban_list_addresses[address[0]][1] \
                    #     and address[1] < ban_list_addresses[address[0]][0] :
                    #     user.send(enc('GG'))
                        
                    #     break
        
                else:
                    print('User {0[0]}:{0[1]} connected as {1}'.format(address,username))
                    print('\n Now connected: \n')
            
                    user.send(enc('Auf ok'))
                    return username

if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    addrs = []

    users = dict()
    try:
        while True:
            user, address = server_socket.accept()
            print('\n Connected: ', address)
            username = server_auth(user)
            if username:
                users[username] = address
                pprint(users)
                threading.Thread(target = new_client, \
                    args = (user, username)).start()
            else:
                user.send(enc('\nUor are in ban list'))

            
        
    except KeyboardInterrupt:
        print('n\Server shut down!')
        server_socket.close()
    except Exception as e:
        print(e)
        server_socket.close()
    server_socket.close()