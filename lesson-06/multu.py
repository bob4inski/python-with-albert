from rest import res as dumai
import multiprocessing,os

def rabotai(spisok:list,a,b):
    for i in spisok:
        process = multiprocessing.Process(target = dumai,args = (i,a,b))
        process.start()





ars = ['ad.txt','ad1.txt','ad2.txt','ad3.txt','ad4.txt']
rabotai(ars,'cat','dog')
