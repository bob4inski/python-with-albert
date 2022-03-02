import filecmp
import hashlib
import os
def stat(file):
    a = ['uid','gid']
    information = os.stat(file)
    result,b = [],[]
    result.append(a)
    b.append(information.st_uid)
    b.append(information.st_gid)
    result.append(b)
    return result

#for i,j in zip(stat('/home/robert/homework.txt')):
#    print(i,j)
#stat('/home/robert/homework.txt')


def papka(roadtofile):
    c = roadtofile.split('/')
    del c[-1]
    roadtofolder = '/'.join(c) 
    print(roadtofolder)
    files = os.listdir(roadtofolder)
    dict_files = { fn:(os.stat(fn).st_mtime) for fn in files}
    items = dict_files.items()
    items = sorted(items, key = lambda x:x[1])
    for pair in items:
        print(pair[0])

def rm_duplicates(dir1,dir2):
    same = filecmp.dircmp(dir1,dir2).same_files
    for fn in same:
        f1,f2 = ''
        with open(dir1 + '/' + fn,'r') as f:
            f1 = f.read()
        with open(dir2 + '/' + fn,'r') as f:
            f2 = f.read()
        h1 = hashlib.sha224(f1.encode('untf-8')).hexdigest()
        h2 = hashlib.sha224(f2.encode('untf-8')).hexdigest()
        if h1 == h2:
            print('удалять этот хлам?')
        c = read()
        if c == 'yes':
            os.remove(dir2 + '/' + fn)



papka('/home/robert/homework.txt')