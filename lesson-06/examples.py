import matplotlib.pyplot as pt

#pt.pie([20,20,60],colors = ['red','blue','green'] , startangle=90,autopct='%1.2f%%')

pt.show()
def arr(*args):
    f = args[-1]
    d = 0
    for i in (args[:-1]):
        pt.plot(i[0],i[1],color = f[d])
        d += 1


    pt.show()
arr(([1,2,3,4],[2,3,4,5]),([0,1,1,1],[2,3,4,5]),['red','green'])

def question():
    count = int(input('Скока'))
    for i in range(count):
        x = input().split(' ')
        y = input().split(' ')
        color = input()
        pt.plot(x,y,color)
    pt.show()

def arrsen(x,y,colors,title = '',xlabel = '',ylable = ''):

    if xlabel:
        pt.xlabel= 'rt'
    if ylable:
        pt.ylabel = 'tt'
    if title:
        pt.title = title

    bars = pt.bar(x, y)
    i = 0
    while i < len(colors) and i < len(bars):
        bars[i].set_color(colors[i])
    pt.show()

def draw(*args):
    piecew = []
    colorss = []
    labelss = []
    for i in args:
        piecew.append(i[0])
        labelss.append(i[1])
        colorss.append(i[2])
    pt.pie(piecew, colors = colorss,startangle=90,autopct='%1.2f%%')
    pt.legend(labelss)
    pt.show()
#draw([10,'baran','red'],[10,'ban','green'])



