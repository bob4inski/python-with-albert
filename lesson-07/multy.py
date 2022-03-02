def buble(a):
    Nh = len(a)
    for i in range(Nh-1):
        for j in range(Nh-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def sort1(array=[12,4,5,6,7,3,1,15]):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort1(less)+equal+sort1(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


import matplotlib.pyplot as pt
import time
import random

def statik(*args):
    f = args[-1]
    d = 0
    for i in (args[:-1]):
        pt.plot(i[0],i[1],color = f[d])
        d += 1

def timer(array,n = 1):
    t = time.time()
    if n == 1:
        buble(array)
    else:
        sort1(array)
        
    d = time.time()
    return d - t

def graph(stolb,stolb2,strok):
    pt.plot(strok,stolb,color = 'red')
    pt.plot(strok,stolb2,color = 'green')
    pt.show()

def work(wtf):
    times,ns = [],[]
    times2 = []
    sek = 0
    if wtf == 0:
        co = 200
    elif wtf == 1:
        co = 250
    else:
        co = 300
    for i in range(co,6000,150):
        N = []
        for f in range(i):
            N.append(random.randint(0,100))
        random.shuffle(N)
        Nav = N.copy()
        sek = timer(N)
        sek2 = timer(Nav,2)
        times.append(sek)
        times2.append(sek2)
        ns.append(i)
    graph(times,times2,ns)

import multiprocessing,os

def rabotai():
    for i in range(3):
        process = multiprocessing.Process(target = work,args = (i,))
        process.start()


rabotai()