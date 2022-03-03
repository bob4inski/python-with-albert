from operator import truediv
import os
import netifaces
from asyncore import read
import subprocess
def systema():
    a = os.uname()
    if a.sysname == 'Linux':
        print(a.version)
        print(a.release)
        print(a.sysname)
def intner(n = 1):
    print('У вас есть несколько интерфейсов , напишите название интерфейса, по которому хотите получить информацию')
    spisok = netifaces.interfaces()
    for i in range(len(spisok)):
        print(i,' ',spisok[i])
    i = int(input())
    c = netifaces.ifaddresses(spisok[i])
    print(c)

def allainbar(primer):
    b = subprocess.getoutput('cat ~/.bash_history').split('\n')
    b = b[::-1]
    print(b)
    for i in b:
        if primer in i:
            print(i)
            print('ввести команду?')
            f = input()
            if f == 'да' or f =='y':
                os.system(i)
                break
            elif f == 'q':
                break
        

    
#def inter(n == 1):
allainbar('python3')