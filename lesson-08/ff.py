
import os
def papka(roadtofile):
    c = roadtofile.split('/')
    del c[-1]
    roadtofolder = '/'.join(c) 
    print(roadtofolder)
    files = os.listdir(roadtofolder)
    print(files)
    dict_files = { fn:(os.stat(fn).st_mtime) for fn in files}
    items = dict_files.items()
    items = sorted(items, key = lambda x:x[1])
    for pair in items:
        print(pair[0])


papka('/home/robert/homework.txt')