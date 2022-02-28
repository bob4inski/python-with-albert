from operator import truediv
import os
def da():
    a = os.uname()
    return a.sysname == 'Linux'

a = os.uname()
def res(n,a,b):
    if os.path.exists(n) and os.path.isfile(n):
        if n[-4:] == '.txt':
            filee = open(n,'r')
            d = filee.read()
            print(d)
            d = d.replace(a,b)
            print(d)
            filee.close()
            filee = open(n,'w')
            filee.write(d)
            filee.close()