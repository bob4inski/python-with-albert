import argparse
import sys
import os
import tarfile

parser = argparse.ArgumentParser()
parser.add_argument('-f','--file')
args = parser.parse_args(sys.argv[1:])
print(args.file)

def  work(a , b ):
    archiv = tarfile.open(b,'w|gz')
    archiv.add(a)






work(args.file,args.folder)