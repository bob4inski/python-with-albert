import argparse
import sys
import os
import tarfile

parser = argparse.ArgumentParser()
parser.add_argument('-f','--file')
parser.add_argument('-fol','--folder',default = 'archive.tar.gz')
parser.add_argument('-o','--output')
parser.add_argument('-n','--number')

args = parser.parse_args(sys.argv[1:])
print(args.file)
# def work():
#     if num = 1:
#         file_und_fold(a,b)


def  file_und_fold(a , b ):
    archiv = tarfile.open(b,'w|gz')
    archiv.add(a)

def only_f(a):
    foldername = a[:-4] + '.tar.gz'
    archiv = tarfile.open(foldername,'w|gz')
    archiv.add(a)

def wal(arr):
    fold = arr.folder
    route = os.walk(fold)
    archiv = tarfile.open(fold + '.tar.gz','w|gz')
    for  root,dir,files in route:
        for file in files:
            archiv.add(os.path.join(root,file))
            print(os.path.join(root, file))
    archiv.close()


wal(args)