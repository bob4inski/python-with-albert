import os
import subprocess
import socket

with open ('servers.txt') as file:
    for address in file:
        host_port = address.split(':')
        HOST,PORT = host_port[0],int(host_port[1])
        connection = socket.socket()
        try:
            connection.settimeout(5)
            connection.connect((HOST,PORT))
            
        except Exception as e:
            print(f'Server {HOST} is unreachable')
            print(e)
        else:
            print(f'Ok {HOST}')
        finally:
            connection.close()
      

            


        

