import tarfile

from click import command
import os
t = tarfile.open('new.tar.gz','w|gz')
f = open('new.txt','w')
s = 'это тестовая строка'
for i in range(1000000):
    f.write(s+'/')
    print(i)
t.add('new.txt')

command = 'ls -l |grep new'
os.system(command)
t.close()