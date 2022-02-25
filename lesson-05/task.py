import matplotlib.pyplot as pt
def arr(*args):
    f = args[-1]
    d = 0
    for i in (args[:-1]):
        pt.plot(i[0],i[1],color = f[d])
        d += 1


    pt.show()
#arr(([1,2,3,4],[2,3,4,5]),([0,1,1,1],[2,3,4,5]),['red','green'])

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
        pt.xlabel= xlabel
    if ylable:
        pt.ylabel = ylable
    if title:
        pt.title = title

    bars = pt.bar(x, y)
    i = 0
    while i < len(colors) and i < len(bars):
        bars[i].set_color(colors[i])
    pt.show()

arrsen(['ну а что гвоорить ','блять ну хуй'],[1,2],'red')
